import boto3
import json

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

table = dynamodb.Table('Sneakers')

with open("sneakerdata.json") as json_file:
    Sneakers = json.load(json_file)
    for sneaker in Sneakers:
        brand = sneaker['brand']
        model = sneaker['model']

        print("Adding sneaker:", brand, model)

        table.put_item(
           Item={
               'brand': brand,
               'model': model,
            }
        )
