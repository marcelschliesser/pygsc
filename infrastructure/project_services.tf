resource "google_project_service" "apis" {
  for_each                   = toset(var.apis)
  service                    = each.value
  disable_dependent_services = true
}