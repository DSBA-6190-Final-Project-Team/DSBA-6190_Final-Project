setup:
	python3 -m venv .DSBA-6190_Final-Project

install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	#Pytest is throwing errors when looking at the IMGS directory, which 
	#is only maintained locally, due to it's large size. Until I can determine
	#how to ignore calls to this directory the test will be commented out.
	
	#python -m pytest --nbval notebooks/processing_upload2s3.ipynb
	#python -m pytest --nbval notebooks/model_training_and_endpoint_deployment.ipynb
	python -m pytest --nbval notebooks/evaluate_deployed_endpoint.ipynb

lint:
	pylint --disable=R,C,W0613			REST_API/lambda_function.py
	pylint --disable=R,C,W1202,W0201	load_test/*.py

all: 
	install lint test