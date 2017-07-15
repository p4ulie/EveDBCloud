from __future__ import print_function # Python 2/3 compatibility
import boto3
from boto3.dynamodb.conditions import Key, Attr
from botocore.exceptions import ClientError

def table_invCategories(dynamodb_resource):
    dynamodb_table = None
    try:
        dynamodb_table = dynamodb_resource.create_table(
            TableName='eve-db-invCategories',
            KeySchema=[
                {
                    'AttributeName': 'categoryID',
                    'KeyType': 'HASH'  # Partition key
                },
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'categoryID',
                    'AttributeType': 'N'
                },
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            }
        )
    except ClientError as ce:
        if ce.response['Error']['Code'] == 'ResourceInUseException':
            dynamodb_table = dynamodb_resource.Table('eve-db-invCategories')
        else:
            print(ce.response['Error'])

    return dynamodb_table

def table_invGroups(dynamodb_resource):
    dynamodb_table = None
    try:
        dynamodb_table = dynamodb_resource.create_table(
            TableName='eve-db-invGroups',
            KeySchema=[
                {
                    'AttributeName': 'groupID',
                    'KeyType': 'HASH'  # Partition key
                },
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'groupID',
                    'AttributeType': 'N'
                },
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            }
        )
    except ClientError as ce:
        if ce.response['Error']['Code'] == 'ResourceInUseException':
            dynamodb_table = dynamodb_resource.Table('eve-db-invGroups')
        else:
            print(ce.response['Error'])

    return dynamodb_table

def table_invTypes(dynamodb_resource):
    dynamodb_table = None
    try:
        dynamodb_table = dynamodb_resource.create_table(
            TableName='eve-db-invTypes',
            KeySchema=[
                {
                    'AttributeName': 'typeID',
                    'KeyType': 'HASH'  # Partition key
                },
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'typeID',
                    'AttributeType': 'N'
                },
                {
                    'AttributeName': 'groupID',
                    'AttributeType': 'N'
                },
                {
                    'AttributeName': 'categoryID',
                    'AttributeType': 'N'
                },
                {
                    'AttributeName': 'typeName',
                    'AttributeType': 'S'
                },
            ],
            GlobalSecondaryIndexes=[
                {
                    'IndexName': 'group',
                    'KeySchema': [
                        {
                            'AttributeName': 'groupID',
                            'KeyType': 'HASH'
                        }
                    ],
                    'Projection': {
                        'ProjectionType': 'ALL'
                    },
                    'ProvisionedThroughput': {
                        'ReadCapacityUnits': 1,
                        'WriteCapacityUnits': 1
                    }
                },
                {
                    'IndexName': 'category',
                    'KeySchema': [
                        {
                            'AttributeName': 'categoryID',
                            'KeyType': 'HASH'
                        }
                    ],
                    'Projection': {
                        'ProjectionType': 'ALL'
                    },
                    'ProvisionedThroughput': {
                        'ReadCapacityUnits': 1,
                        'WriteCapacityUnits': 1
                    }
                },
                {
                    'IndexName': 'name',
                    'KeySchema': [
                        {
                            'AttributeName': 'typeName',
                            'KeyType': 'HASH'
                        }
                    ],
                    'Projection': {
                        'ProjectionType': 'ALL'
                    },
                    'ProvisionedThroughput': {
                        'ReadCapacityUnits': 1,
                        'WriteCapacityUnits': 1
                    }
                }
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            }
        )

        print("Waiting for table [{}] to be created".format('eve-db-invTypes'))
        waiter = dynamodb_table.meta.client.get_waiter('table_exists')
        waiter.wait(TableName='eve-db-invTypes')
        # if no exception, continue
        print("Table created.")

    except ClientError as ce:
        if ce.response['Error']['Code'] == 'ResourceInUseException':
            dynamodb_table = dynamodb_resource.Table('eve-db-invTypes')
        else:
            print(ce.response['Error'])

    return dynamodb_table