variable "aws_account_id" {}
variable "aws_access_key" {}
variable "aws_secret_key" {}
variable "aws_region" {}

variable "apigateway_stage_name" {}

variable "api_version" {}

provider "aws" {
    access_key = "${var.aws_access_key}"
    secret_key = "${var.aws_secret_key}"
    region = "${var.aws_region}"
}
