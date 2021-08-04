import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

table = dynamodb.create_table(
    TableName='Sneakers',
    KeySchema=[
        {
            'AttributeName': 'brand',
            'KeyType': 'HASH'  #Partition key
        },
        {
            'AttributeName': 'model',
            'KeyType': 'RANGE'  #Sort key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'brand',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'model',
            'AttributeType': 'S'
        },

    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }
)

print("Table status:", table.table_status)