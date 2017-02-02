# kinesis-to-bigquery
An AWS lambda function to send data from Kinesis to Google BigQuery

* Clone this repo
* [Include google application default credentials json on project root folder](https://developers.google.com/identity/protocols/application-default-credentials)
* Install google api client dependencies

```pip install --upgrade google-api-python-client```

* Set your Google project id, dataset and tablename
* Zip folder content
* Upload to AWS Lambda, set the python filename as lambda handler
* Set GOOGLE_APPLICATION_CREDENTIALS as environment variable key and your credentials json file name as value on AWS Lambda management

