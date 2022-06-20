terraform {}

provider "google" {
  project = var.project_id # test project
  region  = var.region
}

locals {
  default_labels = {
    "provisioner" = "terraform",
    "git_project" = "pygsc"
  }
}