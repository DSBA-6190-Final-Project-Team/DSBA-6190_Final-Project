# Steps for Setting Up REST API with API Gateway and Lambda Function
## REST API Accepts Binary Images (JPG) and Returns JSON Payload

The following blog post was a big help in setting up the SageMaker endpoint as a REST API, able to accept binary JPG files: 

[**AWS Compute Blog**: Binary Support for API Integrations with Amazon API Gateway](https://aws.amazon.com/blogs/compute/binary-support-for-api-integrations-with-amazon-api-gateway/) (Accessed on 4/24/2020)

### Create Resource and Method
1. Go to AWS API Gateway. Select **Create API**
IMAGE - 1

2. Select **REST API**. Click Build.

3. Keep Defaults. Add Name and description.

4. Go to **Resources** (Left bar, under API): . Make Sure **/** is highlighted in the **Resources** banner.
IMAGE - 2

5. Select **Actions > Create Resource**.
 
6. Enter Resource Name. Maintain all other defaults.

7. Ensure **Resources** is selected under __API: {Resource Name}__. In **Resources** left side banner ensure **/{Resource Name}** is highligthed. Select **Actions > Create Method**.

8. Select **POST** from drop-down. Click check mark.

### Configure Method
1. With **POST** highlighted, select:
* Integration type: Lambda Function
* Use Lambda Proxy Integration: NOT checked
* Lambda Region: Ensure region is consistent with Lambda we are connecting the API to.
* Lambda Function: Enter lambda function name
* Use Default Timeout: Remain checked.
* Clcik Save. Select OK to give API Gateway permission to invoke Lambda Function.

Image -3 

2. Click on Integration Request

Image - 4

3. Click **Mapping Templates** so that drop-down content is visible.

4. For **Request body passthrough**, select **When there are no templates defined (recommended)**.

5. Under Content-Type, click **Add mapping template**.

6. Add **image/jpg**. Click check mark.

7. Scroll Down. Enter the following in the empty template box.

Image - 5 



