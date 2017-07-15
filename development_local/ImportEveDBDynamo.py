from __future__ import print_function  # Python 2/3 compatibility

import csv

import boto3

import DynamoDB_create_eve_tables


def load_invCategories(file):
    categories = {}

    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            category = {}

            categoryID = int(row['categoryID'])
            category['categoryID'] = categoryID
            category['categoryName'] = row['categoryName']

            categories[categoryID] = category

    return categories

def load_invGroups(file):
    groups = {}

    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            group = {}

            groupID = int(row['groupID'])
            group['groupID'] = groupID
            group['categoryID'] = int(row['categoryID'])
            group['groupName'] = row['groupName']

            groups[groupID] = group

    return groups

def load_invTypes(file):
    types = {}

    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)
        type = {}
        for row in reader:
            type = {}

            typeID = int(row['typeID'])
            type['typeID'] = typeID
            if row['typeName'] != '':
                type['typeName'] = row['typeName']
            if row['description'] != '':
                type['description'] = row['description']
            type['groupID'] = int(row['groupID'])

            types[typeID] = type

    return types

def write_items_to_DB(table, items):
    with table.batch_writer() as batch:
        for item in items.itervalues():
            batch.put_item(Item=item)

def main():
    # Get the resource
    dynamodb_resource = boto3.resource('dynamodb',
                                       region_name='local',
                                       aws_access_key_id="anything",
                                       aws_secret_access_key="anything",
                                       endpoint_url="http://localhost:8000")

    # download export files from S3
    # s3 = boto3.client('s3')
    # s3.download_file("eve-db-dump", "invCategories.csv", "invCategories.csv")
    # s3.download_file("eve-db-dump", "invGroups.csv", "invGroups.csv")
    # s3.download_file("eve-db-dump", "invTypes.csv", "invTypes.csv")

    # create dynamodb tables
    table_categories = DynamoDB_create_eve_tables.table_invCategories(dynamodb_resource)
    table_groups = DynamoDB_create_eve_tables.table_invGroups(dynamodb_resource)
    table_types = DynamoDB_create_eve_tables.table_invTypes(dynamodb_resource)

    # load categories
    categories = load_invCategories('invCategories.csv')
    write_items_to_DB(table_categories, categories)

    # load groups
    groups = load_invGroups('invGroups.csv')
    write_items_to_DB(table_groups, groups)

    # load invTypes
    types = load_invTypes('invTypes.csv')
    # add categoryID to type, from groups
    for type in types.itervalues():
        type['categoryID'] = groups[type['groupID']]['categoryID']
    write_items_to_DB(table_types, types)


if __name__ == '__main__':
    main()