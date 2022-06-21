resource "google_project_service" "gsc_api" {
  project = var.project_id
  service = "searchconsole.googleapis.com"
}

resource "google_project_service" "iam_creds" {
  project = var.project_id
  service = "iamcredentials.googleapis.com"
}