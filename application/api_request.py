#https://developers.google.com/api-client-library/python/auth/service-accounts
#https://developers.google.com/webmaster-tools/search-console-api-original/v3/quickstart/quickstart-python

from google.oauth2 import service_account
import googleapiclient.discovery

SCOPES = ['https://www.googleapis.com/auth/webmasters.readonly']
SERVICE_ACCOUNT_FILE = 'key.json'

credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)

webmasters_service = googleapiclient.discovery.build('webmasters', 'v3', credentials=credentials)

request = {
    'startDate': '2019-01-10',
    'endDate': '2019-01-10',
    'dimensions': ['query'],
    'rowLimit': 25000
    }

response = webmasters_service.searchanalytics().query(siteUrl='https://www.xyz.de/', body=request).execute()

print(response)
