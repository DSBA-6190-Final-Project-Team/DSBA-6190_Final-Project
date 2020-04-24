from flask import Flask, request, render_template
from flask.logging import create_logger
import logging

# Import from Python Scripts
#from python_scripts.model import InputForm
#from python_scripts.custom_functions import create_dataframe, scale

app = Flask(__name__)
LOG = create_logger(app)
LOG.setLevel(logging.INFO)


# App Pages

@app.route("/")
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)