resource "google_bigquery_dataset" "dataset" {
  dataset_id    = "google_search_console"
  friendly_name = "google_search_console"
  description   = "Hold the data from the Google Search Console"
  location      = var.region

  labels = merge(local.default_labels, {})


}