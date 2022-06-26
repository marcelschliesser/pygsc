resource "google_bigquery_dataset" "dataset" {
  dataset_id    = "google_search_console"
  friendly_name = "google_search_console"
  description   = "Hold the data from the Google Search Console"
  location      = var.region
  labels        = merge(local.default_labels, {})
}

resource "google_bigquery_table" "default" {
  deletion_protection = false
  dataset_id          = google_bigquery_dataset.dataset.dataset_id
  table_id            = "google_search_console_data"

  time_partitioning {
    type  = "DAY"
    field = "date"
  }

  labels = merge(local.default_labels, {})

  schema = file("bigquery_schema/google_search_console_data_table.json")

}