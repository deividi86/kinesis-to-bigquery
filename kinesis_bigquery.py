import uuid
from googleapiclient import discovery
from oauth2client.client import GoogleCredentials
import base64
import ast


def lambda_handler(event, context):
    for record in event['Records']:
        payload = base64.b64decode(record['kinesis']['data'])

    credentials = GoogleCredentials.get_application_default()
    service = discovery.build('bigquery', 'v2', credentials=credentials)

    project_id = '<google_project_id>'
    dataset_id = '<bigquery_dataset_id>'
    table_id = '<bigquery_tablename>'

    row = ast.literal_eval(payload)

    insert_all_data = {
        'rows': [{
            'json': row,
            'insertId': str(uuid.uuid4()),
        }]
    }

    response = service.tabledata().insertAll(
        projectId=project_id,
        datasetId=dataset_id,
        tableId=table_id,
        body=insert_all_data).execute(num_retries=5)

    return response
