import logging
import os
import json
import posixpath
import boto3
import base64

# Define Temporary Image Location
image_location = "/tmp/photo.jpg"

# Establish Region
region = "us-east-1"

# Define Endpoint
endpoint_name = os.environ['ENDPOINT_NAME']

# Establish Boto3 Session
boto_sess = boto3.session.Session(region_name=region)

# Invoke SageMaker Runtime Client
runtime = boto_sess.client(service_name='runtime.sagemaker')

logger = logging.getLogger()
logger.setLevel(logging.INFO)

logger.error('Starting prediction')


def write_to_file(save_path, data):
  with open(save_path, "wb") as f:
    f.write(base64.b64decode(data))

def image_to_bytearray(save_path):
    with open(save_path, 'rb') as f:
        payload = f.read()
        payload = bytearray(payload)  
    return payload

def invoke_endpoint(payload):
    response = runtime.invoke_endpoint(EndpointName=endpoint_name, 
                                       ContentType='application/x-image', 
                                       Body=payload)
    result = response['Body'].read()
    result = json.loads(result)
    return result

def lambda_handler(event, context):
    
    # Writes Image to Local Temp File
    write_to_file(image_location, event["base64Image"])
    
    # Converts Image to Byte Array
    image_bytearray = image_to_bytearray(image_location)
    
    # Generates Prediction with Byte Array. 
    # Returns List of Probabilites for All Classes
    payload = invoke_endpoint(image_bytearray)
    
    #print(payload)
    
    payload_test = "1, 2, 3"
    
    return {'payload' : payload}
