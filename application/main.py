import google.auth
import argparse
from google.auth import impersonated_credentials
import googleapiclient.discovery
from google.cloud import bigquery


parser = argparse.ArgumentParser()

parser.add_argument("domain")
args = parser.parse_args()

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

dimensions = ['date', 'country', 'device', 'page', 'query']

request = {
    'startDate': '2022-01-01',
    'endDate': '2022-01-03',
    'dimensions': dimensions,
    'rowLimit': 10
    }


def prepare_data_bigquery(data):
    out = list()
    for row in data['rows']:
        mapped = dict(zip(dimensions, row['keys']))
        del row['keys']
        out.append(mapped | data['rows'][0])
    return out



response = search_console_service.searchanalytics().query(siteUrl=f'sc-domain:{args.domain}', body=request).execute()

data_in = prepare_data_bigquery(response)
print(data_in)

client = bigquery.Client()
client.load_table_from_json([data_in], 'onyx-dragon-349408.google_search_console.google_search_console_data')

