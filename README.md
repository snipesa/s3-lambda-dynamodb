# s3-lambda-dynamodb
Architecture is designed such that any json upload/update to an existing bucket with specific location will trigger a lambda function. This function has a runtime  with steps to get objects from that s3 bucket and input to a specific dynamoDB table with a given format.

S3 BUCKET
An s3 bucket is created where files could be stored in any format(.txt,.json,.xml, etc)
LAMBDA
Role attached to lambda function should have permission for s3(read, and get object), DynamoDB(read, put), and cloudwatch logs
A trigger is attached to the lambda function for s3 put actions with suffix ".json"
Make sure to configure the function timeout seconds for it to run successfully
The function makes use of boto3 and json libraries
DYNAMODB
The lambda function autommatically creates a dynamodb if one does not exist and inputes the data into it

Reference info:
online json viewer: jsonviewer.stack.hu           ..records...(copied from cloud watch logs)
Boto Docs: for both dynamodb and s3
