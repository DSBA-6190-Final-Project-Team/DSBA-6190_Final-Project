setup:
	python3 -m venv .DSBA-6190_Final-Project

install:
	pip install -r requirements.txt

test:
	#python -m pytest -vv --cov=myrepolib tests/*.py
	#python -m pytest --nbval wine_predict/wine_quality_predict.ipynb

lint:
	#hadolint Dockerfile 
	pylint --disable=R,C wine_predict/*.py

	
all: 
	install lint test