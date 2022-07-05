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
    lifetime=60)

search_console_service = googleapiclient.discovery.build(
    'searchconsole',
    'v1',
    credentials=target_credentials,
    cache_discovery=False)

dimensions = ['date', 'country', 'device', 'page', 'query']


def call_google_search_console_api(date: str):
    return_data = list()
    index = 0
    row_limit = 25000

    while True:
        payload = {
            'startDate': date,
            'endDate': date,
            'searchType': 'web',
            'dimensions': dimensions,
            'rowLimit': row_limit,
            "startRow": row_limit * index
        }

        chunk = search_console_service.searchanalytics().query(
            siteUrl=f'sc-domain:{args.domain}',
            body=payload).execute()

        index += 1

        if 'rows' in chunk.keys():
            return_data.extend(chunk['rows'])
        else:
            break

    return return_data


def prepare_data_bigquery(data):
    """
    Map the Values to the Dimensions. And add alle KPIs like clicks etc.
    """
    out = list()
    for row in data:
        mapped = dict(zip(dimensions, row['keys']))
        del row['keys']
        out.append(mapped | row)
    return out


date = "2022-01-01"
gsc_data = call_google_search_console_api(date=date)

gsc_data_transformed = prepare_data_bigquery(gsc_data)

job_config = bigquery.LoadJobConfig()
job_config.write_disposition = bigquery.WriteDisposition.WRITE_TRUNCATE
job_config.time_partitioning = bigquery.TimePartitioning(field="date")

bigquery_client = bigquery.Client()
table_ref = bigquery_client.dataset('google_search_console').table(f'google_search_console_data${date.replace("-", "")}')

bigquery_client.load_table_from_json(
    json_rows=gsc_data_transformed,
    destination=table_ref,
    job_config=job_config
    )
