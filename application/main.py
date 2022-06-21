import google.auth
from google.auth import impersonated_credentials
import googleapiclient.discovery

target_scopes = ["https://www.googleapis.com/auth/webmasters.readonly"]
source_credentials, project_id = google.auth.default()
target_credentials = impersonated_credentials.Credentials(
    source_credentials=source_credentials,
    target_principal='bigquery-exporter@onyx-dragon-349408.iam.gserviceaccount.com',
    target_scopes=target_scopes,
    lifetime=500)

search_console_service = googleapiclient.discovery.build(
    'searchconsole',
    'v1',
    credentials=target_credentials,
    cache_discovery=False)


site_list = search_console_service.sites().list().execute()
print(site_list)


request = {
    'startDate': '2022-01-01',
    'endDate': '2022-01-03',
    'dimensions': ['query'],
    'rowLimit': 25000
    }

#response = search_console_service.searchanalytics().query(siteUrl='sc-domain:', body=request).execute()

#print(response)
