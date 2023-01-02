from boto3 import resource, client
from dotenv import load_dotenv
import os

load_dotenv()

dynamodb = resource('dynamodb')
dynamodb_client = client('dynamodb')

tablename = os.getenv('TABLENAME')
table = dynamodb.Table(tablename)

existingtables = dynamodb_client.list_tables()['TableNames']

def checkIfTableExist():
    if tablename not in existingtables:
        print('La tabla {} no existe'.format(tablename))
        dynamodb.create_table(
        TableName='christmaslist',
        KeySchema=[
            {
                'AttributeName': 'child',
                'KeyType': 'HASH'
            },
            {
                'AttributeName': 'id',
                'KeyType': 'RANGE'
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'child',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'id',
                'AttributeType': 'N'
            }
        ],
        ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
        }   
    )
        print('La tabla {} se a creado'.format(tablename))

def checkIfItemExist():
    return 'hola'
def addItemToList(child, id, city, text, gifts):
    table.put_item(
    Item={
            'child': child,
            'id': int(id),
            'city': city,
            'text': text,
            'gifts': gifts.split(", ")
        }
    )

def getItemFromList():
    pass