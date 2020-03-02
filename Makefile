setup:
	python3 -m venv .DSBA-6190_Final-Project

install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	#python -m pytest -vv --cov=myrepolib tests/*.py
	#python -m pytest --nbval wine_predict/wine_quality_predict.ipynb

lint:
	#hadolint Dockerfile 
	pylint --disable=R,C,W0104,E0602 wine_predict/**.ipynb

run:
	python3 main.py
	
all: 
	install lint test