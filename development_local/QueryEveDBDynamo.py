from __future__ import print_function # Python 2/3 compatibility
import boto3
from boto3.dynamodb.conditions import Key, Attr
from botocore.exceptions import ClientError
import json

def get_category_by_categoryID(dynamodb_table, categoryID):
    item = None
    try:
        response = dynamodb_table.get_item(
            Key={
                    'categoryID': categoryID
                }
        )
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        item = response['Item']

    return item

def get_intType_by_typeID(dynamodb_table, typeID):
    item = None
    try:
        response = dynamodb_table.get_item(
            Key={
                    'typeID': typeID
                }
        )
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        item = response['Item']

    return item

def get_intType_by_groupID(table_types, groupID, limit=-1):
    response = None
    try:
        response = table_types.query(
            IndexName='group',
            KeyConditionExpression=Key('groupID').eq(groupID),
        )
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        pass

    return response

def get_intType_by_categoryID(table_types, categoryID, limit=-1):
    response = None
    try:
        response = table_types.query(
            IndexName='category',
            KeyConditionExpression=Key('categoryID').eq(categoryID),
        )
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        pass

    return response

def main():
    # Get the resource
    dynamodb_resource = boto3.resource('dynamodb',
                                       region_name='local',
                                       aws_access_key_id="anything",
                                       aws_secret_access_key="anything",
                                       endpoint_url="http://localhost:8000")

    dynamodb_client = boto3.client('dynamodb',
                                   region_name='local',
                                   aws_access_key_id="anything",
                                   aws_secret_access_key="anything",
                                   endpoint_url="http://localhost:8000")

    table_types = dynamodb_resource.Table('eve-db-invTypes')
    table_categories = dynamodb_resource.Table('eve-db-invCategories')


    # items = get_category_by_categoryID(table_categories, 1)
    # response = get_intType_by_groupID(table_types, 18)
    response = get_intType_by_categoryID(table_types, 18)

    items = response['Items']

    print(items)

    for item in items:
        print(item)


if __name__ == '__main__':
    main()