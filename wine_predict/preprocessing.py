
import argparse
import os
import warnings

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from sklearn.exceptions import DataConversionWarning
warnings.filterwarnings(action='ignore', category=DataConversionWarning)

seed = 5590

if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--train-test-split-ratio', type=float, default=0.2)
    args, _ = parser.parse_known_args()
    
    print('Received arguments {}'.format(args))
    
    input_data_path = os.path.join('/opt/ml/processing/input', 'winequality-red.csv')
    
    print('Reading input data from {}'.format(input_data_path))
    df = pd.read_csv(input_data_path, header=0, delimiter=";", low_memory=False)
    
    print()
    
    #Replace spaces in column headers with underscores
    #df.columns = df.columns.str.replace(' ', '_')
    
    #X_columns = df.drop('quality', axis=1).columns
    
    split_ratio = args.train_test_split_ratio
    print('Splitting data into train and test sets with ratio {}'.format(split_ratio))
    #Split Data into training / test
    X_train, X_test, y_train, y_test = train_test_split(df.drop('quality', axis=1), 
                                                        df['quality'], 
                                                        test_size=split_ratio, 
                                                        random_state=seed)
    
    # Transform Features
    scaler = StandardScaler().fit(X_train)
    train_features = scaler.transform(X_train)
    test_features = scaler.transform(X_test)
    
    # Convert Training Data to Float32
    train_features = train_features.astype('float32')
    
    
    # Create local output directories
    try:
        os.makedirs('/opt/ml/processing/output/train')
        os.makedirs('/opt/ml/processing/output/test')
    except:
        pass
    
    print('Train Features shape after preprocessing: {}'.format(train_features.shape))
    print('Train Labels shape after preprocessing: {}'.format(y_train.shape))
    print('Test Features shape after preprocessing: {}'.format(test_features.shape))
    print('Test Labels shape after preprocessing: {}'.format(y_test.shape))
    
    train_features_output_path = os.path.join('/opt/ml/processing/output/train', 'train_features.csv')
    train_labels_output_path = os.path.join('/opt/ml/processing/output/train', 'train_labels.csv')
    
    test_features_output_path = os.path.join('/opt/ml/processing/output/test', 'test_features.csv')
    test_labels_output_path = os.path.join('/opt/ml/processing/output/test', 'test_labels.csv')
    
    print('Saving training features to {}'.format(train_features_output_path))
    pd.DataFrame(train_features).to_csv(train_features_output_path, header= False, index=False)
    
    print('Saving test features to {}'.format(test_features_output_path))
    pd.DataFrame(test_features).to_csv(test_features_output_path, header=False, index=False)
    
    print('Saving training labels to {}'.format(train_labels_output_path))
    y_train.to_csv(train_labels_output_path, header=False, index=False)
    
    print('Saving test labels to {}'.format(test_labels_output_path))
    y_test.to_csv(test_labels_output_path, header=False, index=False)