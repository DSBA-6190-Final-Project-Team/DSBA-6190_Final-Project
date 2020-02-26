
import os
import pandas as pd
import numpy as np

from sklearn.model_selection import KFold
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV
from sklearn.externals import joblib

seed = 5590

if __name__=="__main__":
    training_data_directory = '/opt/ml/input/data/train'
    train_features_data = os.path.join(training_data_directory, 'train_features.csv')
    train_labels_data = os.path.join(training_data_directory, 'train_labels.csv')
    print('Reading input data')
    
    X_train = pd.read_csv(train_features_data, header=None)
    y_train = pd.read_csv(train_labels_data)
    
    X_train = np.array(X_train)
    y_train = np.array(y_train).ravel()
    
    print(X_train.shape)
    print(y_train.shape)
    
    model = RandomForestRegressor(n_estimators = 100,
                                max_depth = None, 
                                max_features= "sqrt",
                                random_state = seed)
    
    print('Training Random Forest Regression model')
    model.fit(X_train, y_train)
    
    print('Training Complete')
    
    model_output_directory = os.path.join('/opt/ml/model', "model.joblib")
    print('Saving model to {}'.format(model_output_directory))
    joblib.dump(model, model_output_directory)