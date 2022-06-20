resource "google_service_account" "bigquery_exporter" {
  account_id   = "bigquery-exporter"
  display_name = "Exports Data from GSC to BigQuery"
}