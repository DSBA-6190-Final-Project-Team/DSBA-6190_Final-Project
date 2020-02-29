
import argparse
import os

import pandas as pd
import numpy as np

from sklearn.ensemble import RandomForestRegressor
from sklearn.externals import joblib

from sklearn.model_selection import cross_val_score
from sklearn.metrics import mean_squared_error

seed = 5590

# Inference Function
def model_fn(model_dir):
    clf = joblib.load(os.path.join(model_dir, "model.joblib"))
    return clf

if __name__=="__main__":
    
    print('Extracting Arguments')
    parser = argparse.ArgumentParser()
    
    # Hyperparameters
    parser.add_argument('--n-estimators', type=int, default=750)
    parser.add_argument('--max-features', type=str, default='sqrt')
    
    # Directories
    parser.add_argument('--model-dir', type=str, default=os.environ['SM_MODEL_DIR'])
    parser.add_argument('--train', type=str, default=os.environ['SM_CHANNEL_TRAIN'])
    parser.add_argument('--test', type=str, default=os.environ['SM_CHANNEL_TEST'])
    parser.add_argument('--train_file_features', type=str, default = 'train_features.csv')
    parser.add_argument('--train_file_labels', type=str, default = 'train_labels.csv')
    parser.add_argument('--test_file_features', type=str, default = 'test_features.csv')
    parser.add_argument('--test_file_labels', type=str, default = 'test_labels.csv')
    
    args = parser.parse_args()
    
    # Data Paths
    train_features_data = os.path.join(args.train, args.train_file_features)
    train_labels_data = os.path.join(args.train, args.train_file_labels)
    
    #test_features_data = os.path.join(args.test, args.test_file_features)
    #test_labels_data = os.path.join(args.test, args.test_file_labels)
    
    
    print('Reading input data')
    # Import Data
    ## Training
    X_train = pd.read_csv(train_features_data)
    y_train = pd.read_csv(train_labels_data)
    
    ## Test
    #X_test = pd.read_csv(test_features_data)
    #y_test = pd.read_csv(test_labels_data)
    
    # Convert Data to NP Array
    ## Training
    X_train = np.array(X_train)
    y_train = np.array(y_train).ravel()
    
    ## Test
    #X_test = np.array(X_test)
    #y_test = np.array(y_test).ravel()
    
    # Check Data Shape
    print(X_train.shape)
    print(y_train.shape)
    
    # Initialize Random Forest Regressor Model. 
    # Hyperparameters based on earlier local analysis
        
    model = RandomForestRegressor(n_estimators = args.n_estimators,
                                  max_features = args.max_features,
                                  random_state = seed)
    
    print('Training Random Forest Regression model')
    model.fit(X_train, y_train)
    
    print('Training Complete')
    
    # Metrics
    
    mse_neg = cross_val_score(model, X_train, y_train, scoring = 'neg_mean_squared_error', cv=10)
    mse_abs = np.absolute(mse_neg)
    rsme = np.sqrt(mse_abs)
    rsme_avg = np.mean(rsme)
    print('RMSE: {}'.format(rsme_avg))
    
    model_output_directory = os.path.join(args.model_dir, "model.joblib")
    print('Saving model to {}'.format(model_output_directory))
    joblib.dump(model, model_output_directory)