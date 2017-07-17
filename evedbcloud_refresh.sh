#!/bin/sh

TFSTATEFILE="evedbcloud.tfstate"

terraform refresh -var-file=evedbcloud.tfvars -state=${TFSTATEFILE}

