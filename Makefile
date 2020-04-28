setup:
	python3 -m venv .DSBA-6190_Final-Project

install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest --nbval notebooks/processing_upload2s3.ipynb
	#python -m pytest --nbval notebooks/model_training_and_endpoint_deployment.ipynb
lint:
	pylint --disable=R,C,W1202	load_test/*.py
	#pylint --disable=R,C		REST_API/lambda_function.py

all: 
	install lint test