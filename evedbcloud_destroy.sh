#!/bin/sh

TFSTATEFILE="evedbcloud.tfstate"

terraform destroy -var-file=evedbcloud.tfvars -state=${TFSTATEFILE}