import boto3


def create_sneakers_table(dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")

    table = dynamodb.create_table(
        TableName='Brand',
        KeySchema=[
            {
                'AttributeName': 'Brand',
                'KeyType': 'HASH'  # Partition key
            },
            {
                'AttributeName': 'Model',
                'KeyType': 'RANGE'  # Sort key
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'Brand',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'Model',
                'AttributeType': 'S'
            },

        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 10
        }
    )
    return table


if __name__ == '__main__':
    sneakers_table = create_sneakers_table()
    print("Table status:", sneakers_table.table_status)