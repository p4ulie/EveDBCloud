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
