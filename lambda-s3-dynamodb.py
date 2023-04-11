import boto3
import json

# Get the service resource.
dynamodb = boto3.resource('dynamodb')
s3_client = boto3.client('s3')

# Create the DynamoDB table.
def createTable():
    table = dynamodb.create_table(
        TableName='demo10',
        KeySchema=[
            {
                'AttributeName': 'employee_id',
                'KeyType': 'HASH'
            },
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'employee_id',
                'AttributeType': 'S'
            },
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
    )

    # Wait until the table exists.
    table.wait_until_exists()

def lambda_handler(event, context):
    createTable()
    bucket = event['Records'][0]['s3']['bucket']['name']
    object_file_name = event['Records'][0]['s3']['object']['key']
    json_object = s3_client.get_object(Bucket=bucket,Key=object_file_name)
    jsonFileReader = json_object['Body'].read()
    jsonDict = json.loads(jsonFileReader)
    table = dynamodb.Table('demo10')
    table.put_item(Item=jsonDict)
    
    return 'Hello from Lambda!'
