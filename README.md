# openvino
Text , Human Pose , Vehicle detector using pre trained models of openvino toolkit

firstly download OpenVINO Toolkit in you machine according to the instructions given in link given below:
https://software.intel.com/en-us/openvino-toolkit/choose-download

# Deploy Your First Edge App

So far, you've downloaded some pre-trained models, handled their inputs, and learned how
to handle outputs. In this exercise, you'll implement the handling of the outputs of our three
models from before, and get to see inference actually performed by adding these models
to some example edge applications. 

There's a lot of code still involved behind the scenes here. With the Pre-Trained Models 
available with the OpenVINO toolkit, you don't need to worry about the Model Optimizer, but
there is still work done to load the model into the Inference Engine. We won't learn about 
this code until later, so in this case, you'll just need to call your functions to handle the input
and output of the model within the app.

If you do want a sneak preview of some of the code that interfaces with the Inference Engine,
you can check it out in `inference.py`. You'll work out of the `handle_models.py` file, as 
well as adding functions calls within the edge app in `app.py`.


## Testing the apps

To test your implementations, you can use `app.py` to run each edge application, with
the following arguments:
- `-t`: The model type,  which should be one of `"POSE"`, `"TEXT"`, or `"CAR_META"`
- `-m`: The location of the model .xml file
- `-i`: The location of the input image used for testing
- `-c`: A CPU extension file, if applicable. See below for what this is for the workspace.
The results of your output will be saved down for viewing in the `outputs` directory.

As an example, here is an example of running the app with related arguments:

```
python app.py -i "images/blue-car.jpg" -t "CAR_META" -m "/home/workspace/models/vehicle-attributes-recognition-barrier-0039.xml" -c "/opt/intel/openvino/deployment_tools/inference_engine/lib/intel64/libcpu_extension_sse4.so"
```

## Model Documentation

Once again, here are the links to the models, so you can use the **Output** section to help
you get started (there are additional comments in the code to assist):

- Human Pose Estimation: [human-pose-estimation-0001](https://docs.openvinotoolkit.org/latest/_models_intel_human_pose_estimation_0001_description_human_pose_estimation_0001.html)
- Text Detection: [text-detection-0004](http://docs.openvinotoolkit.org/latest/_models_intel_text_detection_0004_description_text_detection_0004.html)
- Determining Car Type & Color: [vehicle-attributes-recognition-barrier-0039](https://docs.openvinotoolkit.org/latest/_models_intel_vehicle_attributes_recognition_barrier_0039_description_vehicle_attributes_recognition_barrier_0039.html)

