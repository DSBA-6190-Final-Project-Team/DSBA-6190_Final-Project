
import json
import os
import tarfile

import pandas as pd
import numpy as np

from sklearn.externals import joblib
from sklearn.metrics import mean_squared_error,r2_score

if __name__=="__main__":
    model_path = os.path.join('/opt/ml/processing/model', 'model.tar.gz')
    print('Extracting model from path: {}'.format(model_path))
    with tarfile.open(model_path) as tar:
        tar.extractall(path='.')
    print('Loading model')
    model = joblib.load('model.joblib')

    print('Loading test input data')
    test_features_data = os.path.join('/opt/ml/processing/test', 'test_features.csv')
    test_labels_data = os.path.join('/opt/ml/processing/test', 'test_labels.csv')

    X_test = pd.read_csv(test_features_data, header=None)
    y_test = pd.read_csv(test_labels_data)
    
    X_test = np.array(X_test)
    y_test = np.array(y_test).ravel()
    
    predictions = model.predict(X_test)

    print('Creating Regression Evaluation Report')
    report_dict = {}
    report_dict['r2'] = r2_score(y_test, predictions)
    report_dict['RSME'] = mean_squared_error(y_test, predictions)

    print('Regression Report Report:\n{}'.format(report_dict))

    evaluation_output_path = os.path.join('/opt/ml/processing/evaluation', 'evaluation.json')
    print('Saving Regression Report to {}'.format(evaluation_output_path))

    with open(evaluation_output_path, 'w') as f:
        f.write(json.dumps(report_dict))