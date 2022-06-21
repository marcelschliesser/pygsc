resource "google_project_service" "gsc_api" {
  project = var.project_id
  service = "iamcredentials.googleapis.com"
}