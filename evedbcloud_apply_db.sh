#!/bin/sh

TFSTATEFILE="evedbcloud_db.tfstate"
OUTFILE="evedbcloud_db.tfout"

terraform apply -var-file=trans.tfvars -state=${TFSTATEFILE} -out=${OUTFILE} -target=aws_dynamodb_table.eve-db-invCategories_dynamodb_table
terraform apply -var-file=trans.tfvars -state=${TFSTATEFILE} -out=${OUTFILE} -target=aws_dynamodb_table.eve-db-invGroups_dynamodb_table
terraform apply -var-file=trans.tfvars -state=${TFSTATEFILE} -out=${OUTFILE} -target=aws_dynamodb_table.eve-db-invTypes_dynamodb_table
