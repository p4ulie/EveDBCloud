#!/bin/sh

TFSTATEFILE="evedbcloud.tfstate"
OUTFILE="evedbcloud.tfout"

terraform plan -var-file=trans.tfvars -state=${TFSTATEFILE} -out=${OUTFILE}

