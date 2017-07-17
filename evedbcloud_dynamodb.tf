resource "aws_dynamodb_table" "eve-db-invCategories_dynamodb_table" {
    name = "eve-db-invCategories"
    read_capacity = 5
    write_capacity = 5
    hash_key = "categoryID"
    attribute {
      name = "categoryID"
      type = "N"
    }
}

resource "aws_dynamodb_table" "eve-db-invGroups_dynamodb_table" {
    name = "eve-db-invGroups"
    read_capacity = 5
    write_capacity = 5
    hash_key = "groupID"
    attribute {
      name = "groupID"
      type = "N"
    }
}

resource "aws_dynamodb_table" "eve-db-invTypes_dynamodb_table" {
    name = "eve-db-invTypes"
    read_capacity = 5
    write_capacity = 5
    hash_key = "typeID"
    attribute {
      name = "typeID"
      type = "N"
    }
    attribute {
      name = "groupID"
      type = "N"
    }
    attribute {
      name = "categoryID"
      type = "N"
    }
    attribute {
      name = "typeName"
      type = "S"
    }
    global_secondary_index {
      name               = "group"
      hash_key           = "groupID"
      write_capacity     = 1
      read_capacity      = 1
      projection_type    = "ALL"
    }
    global_secondary_index {
      name               = "category"
      hash_key           = "categoryID"
      write_capacity     = 1
      read_capacity      = 1
      projection_type    = "ALL"
    }
    global_secondary_index {
      name               = "Name"
      hash_key           = "typeName"
      write_capacity     = 1
      read_capacity      = 1
      projection_type    = "ALL"
    }
}
