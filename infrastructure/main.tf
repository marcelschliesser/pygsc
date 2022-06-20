terraform {}

provider "google" {
  project = var.project_id # test project
  region  = var.region
}