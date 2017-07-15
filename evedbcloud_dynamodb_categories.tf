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
