resource "google_service_account" "bigquery_exporter" {
  account_id   = "bigquery-exporter"
  display_name = "Exports Data from GSC to BigQuery"
}

resource "google_service_account_iam_binding" "account-iam" {
  service_account_id = google_service_account.bigquery_exporter.name
  role               = "roles/iam.serviceAccountTokenCreator"
  members = [
    "user:ms@thinq.digital",
  ]
}