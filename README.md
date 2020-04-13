** Add Distracted Driver Image as Header**

# Continuous Integration and Deployment of Image Classification Model
This repo contains the files for a Continuous Integration/Contiuous Deployment (CI/CD) process for an image classification model to identify distracted drivers. For the CI/CD framework, this project uses Amazon CodeBuild to continously deploy and update the project, and Amazon Sagemaker to train and deploy the resulting model to an endpoint. Load testing of the end point is then performed using by an Amazon Lambda function.

The project flow is broken down into the following steps:

1. Process Input Data and Upload to AWS S3
2. Train Model
3. Deploy Model and Evaluate Performance
4. Load-Test Deployed Endpoint
5. CodeBuild Framework for CI/CD Process

**Insert Process Flow Diagram**

## Process Input Data and Upload to AWS S3
### Data Description
The input data for the model is provided by the [**State Farm Distracted Driver Detection**](https://www.kaggle.com/c/state-farm-distracted-driver-detection) Kaggle competition. The data contains two image directories labeled **train** and **test**, as well as two CSV files. The **train** directory contains  24,424 images broken up into 10 discrete classes. Each class of image is located in a sub-folder of the **train** directory. The ten classes are:

* c0: safe driving
* c1: texting - right
* c2: talking on the phone - right
* c3: texting - left
* c4: talking on the phone - left
* c5: operating the radio
* c6: drinking
* c7: reaching behind
* c8: hair and makeup
* c9: talking to passenger

The **test** directory contains 79,726 unlabeled images.

The two CSV files are as follows:

* sample_submission.csv - a sample submission file in the correct format
* driver_imgs_list.csv - a list of training images, their subject (driver) id, and class id

### Data Processing
Currently all data processing is performed locally, and must be completed manually before loading into the CI/CD framework. Future plans are to integrate this step into fully into the process.

The images provided in the **train** directory are JPG files. The algorithm used to develop the model is the Sagemaker Image Classification algorithm. This algorithm can take input data in two formats: 

1. Raw image files (i.e.: JPG, PNG, etc.)
2. RecordIO - [Apache MXNet file type](https://mxnet.apache.org/api/faq/recordio)

The RecordIO file type is recommended by Amazon, and therefore this is the file type used for this project.

To convert raw image files to a RecordIO format we used the conversion tool (**im2rec.py** python script) provided by [Apache MXNet](https://mxnet.apache.org/api/faq/recordio).
