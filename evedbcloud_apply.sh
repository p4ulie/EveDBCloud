#!/bin/sh

TFSTATEFILE="evedbcloud.tfstate"

terraform apply -var-file=evedbcloud.tfvars -state=${TFSTATEFILE}
