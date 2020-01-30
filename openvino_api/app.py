import argparse
import os

import cv2
import numpy as np

from openvino_api.handle_models import handle_output, preprocessing
from openvino_api.inference import Network
from openvino_api.settings import BASE_DIR

CAR_COLORS = ["white", "gray", "yellow", "red", "green", "blue", "black"]
CAR_TYPES = ["car", "bus", "truck", "van"]


def get_mask(processed_output):
    """
    Given an input image size and processed output for a semantic mask,
    returns a masks able to be combined with the original image.
    """
    # Create an empty array for other color channels of mask
    empty = np.zeros(processed_output.shape)
    # Stack to make a Green mask where text detected
    mask = np.dstack((empty, processed_output, empty))

    return mask


def create_output_image(model_type, image, output):
    """
    Using the model type, input image, and processed output,
    creates an output image showing the result of inference.
    """
    if model_type == "POSE":
        # Remove final part of output not used for heatmaps
        output = output[:-1]
        # Get only pose detections above 0.5 confidence, set to 255
        for c in range(len(output)):
            output[c] = np.where(output[c] > 0.5, 255, 0)
        # Sum along the "class" axis
        output = np.sum(output, axis=0)
        # Get semantic mask
        pose_mask = get_mask(output)
        # Combine with original image
        image = image + pose_mask
        return image
    elif model_type == "TEXT":
        # Get only text detections above 0.5 confidence, set to 255
        output = np.where(output[1] > 0.5, 255, 0)
        # Get semantic mask
        text_mask = get_mask(output)
        # Add the mask to the image
        image = image + text_mask
        return image
    elif model_type == "CAR_META":
        # Get the color and car type from their lists
        color = CAR_COLORS[output[0]]
        car_type = CAR_TYPES[output[1]]
        # Scale the output text by the image shape
        scaler = max(int(image.shape[0] / 1000), 1)
        # Write the text of color and type onto the image
        # cv2.putText(img, text, org, fontFace, fontScale, color[, thickness[, lineType[, bottomLeftOrigin]]]) → None
        image = cv2.putText(image,
                            "Color: {}, Type: {}".format(color, car_type),
                            (2 * scaler, 100 * scaler), cv2.FONT_HERSHEY_COMPLEX_SMALL,
                            1 * scaler, (255, 255, 255), 1 * scaler)
        return image

    elif model_type == "PEDESTRIAN":
        # Get only text detections above 0.5 confidence, set to 255
        bbs = output
        for boundingBox in bbs:
            # print(boundingBox[0], boundingBox[1])
            image = cv2.rectangle(image, tuple(boundingBox[0]), tuple(boundingBox[1]), (0, 0, 255), 10)
        return image


    else:
        print("Unknown model type, unable to create output image.")
        return image


def perform_inference(args):
    """
    Performs inference on an input image, given a model.
    """

    # Create a Network for using the Inference Engine
    inference_network = Network()
    # Load the model in the network, and obtain its input shape
    n, c, h, w = inference_network.load_model(args["m"], args["d"], args["c"])

    # Read the input image
    image = cv2.imread(args["i"])

    # TODO: Preprocess the input image
    preprocessed_image = preprocessing(image, h, w)

    # Perform synchronous inference on the image
    inference_network.sync_inference(preprocessed_image)

    # Obtain the output of the inference request
    output = inference_network.extract_output()

    # TODO: Handle the output of the network, based on args.t
    # Note: This will require using `handle_output` to get the correct
    #       function, and then feeding the output to that function.
    output_func = handle_output(args["t"])
    processed_output = output_func(output, image.shape)

    # Create an output image based on network
    output_image = create_output_image(args["t"], image, processed_output)

    # Save down the resulting image
    mystr = args["i"]
    m = mystr.split('/')[-1]
    output_folder_path = str(BASE_DIR) + "/static/" + str('outputs/')
    if not os.path.isdir(output_folder_path):
        os.makedirs(output_folder_path)
    file_name = BASE_DIR + "/static/outputs/output_{}.png".format(m.split('/')[-1].split('.')[0])
    view_file = ".." + "/static/outputs/output_{}.png".format(m.split('/')[-1].split('.')[0])
    cv2.imwrite(file_name, output_image)
    return view_file


def main(image, type, model):
    """  c : CPU extension file location, if applicable
    d : Device, if not CPU (GPU, FPGA, MYRIAD)
    i : The location of the input image
    m : The location of the model XML file
    t : The type of model: POSE, TEXT or CAR_META
    """
    args = {"c": "/opt/intel/openvino/deployment_tools/inference_engine/lib/intel64/libcpu_extension_sse4.so",
            "d": "CPU",
            "i": str(BASE_DIR) + "/images/" + str(image),
            "m": str(BASE_DIR) + str(model),
            "t": str(type)
            }
    return perform_inference(args)
