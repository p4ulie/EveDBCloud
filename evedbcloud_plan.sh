#!/bin/sh

TFSTATEFILE="evedbcloud.tfstate"
OUTFILE="evedbcloud.tfout"

terraform plan -var-file=evedbcloud.tfvars -state=${TFSTATEFILE} -out=${OUTFILE}

