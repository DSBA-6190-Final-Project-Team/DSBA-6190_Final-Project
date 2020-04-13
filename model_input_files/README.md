# Model Input Files
This folder contains the processed data files of the input images. The data processing method creates three types of files: LST, IDX, and REC. The REC files are RecordIO format, and are the file type uploaded to S3 for use as a model input. 

The RecordIO files, along with any raw images, are excluded from this REPO. The size of these files are too big to inlcude. Please see the notes on the **processing_upload2s3.ipynb** notebook for how to generate the RecordIO files. 
