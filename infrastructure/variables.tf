variable "project_id" {
  type    = string
  default = "onyx-dragon-349408"
}

variable "region" {
  type    = string
  default = "europe-west3"
}

variable "apis" {
  description = "List of apis to enable"
  type        = list(string)
  default = [
    "searchconsole.googleapis.com",
    "iamcredentials.googleapis.com",
    "cloudresourcemanager.googleapis.com" //needed by terraform
  ]
}