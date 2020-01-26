# openvino
Text , Human Pose , Vehicle detector using pre trained models of openvino toolkit

Here is the Live link to this project:  https://www.askai.ga/

firstly download OpenVINO Toolkit in your local machine according to the instructions given in link given below:
https://software.intel.com/en-us/openvino-toolkit/choose-download

## Testing the project locally
1- Create virtual environment
    conda create -n pyvenv
    conda activate pyvenv
2- pip install -r requirements.text
3- python manage.py migrate
4- python manage.py runserver
5- you can find your server running at 127.0.0.0:8000

## Model Documentation

Once again, here are the links to the models, so you can use the **Output** section to help
you get started (there are additional comments in the code to assist):

- Human Pose Estimation: [human-pose-estimation-0001](https://docs.openvinotoolkit.org/latest/_models_intel_human_pose_estimation_0001_description_human_pose_estimation_0001.html)
- Text Detection: [text-detection-0004](http://docs.openvinotoolkit.org/latest/_models_intel_text_detection_0004_description_text_detection_0004.html)
- Determining Car Type & Color: [vehicle-attributes-recognition-barrier-0039](https://docs.openvinotoolkit.org/latest/_models_intel_vehicle_attributes_recognition_barrier_0039_description_vehicle_attributes_recognition_barrier_0039.html)

