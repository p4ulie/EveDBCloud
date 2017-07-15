#!/bin/sh

TFSTATEFILE="evedbcloud.tfstate"
TFSTATEOUTFILE="evedbcloud.tfstateout"

terraform apply -var-file=trans.tfvars -state=${TFSTATEFILE} -state-out=${TFSTATEOUTFILE}
