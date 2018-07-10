from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
from apiclient.http import MediaFileUpload
from oauth2client.service_account import ServiceAccountCredentials
import sys

SCOPES = 'https://www.googleapis.com/auth/drive'
store = file.Storage('storage.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
    creds = tools.run_flow(flow, store)

drive_service = build('drive', 'v3', http=creds.authorize(Http()))

file_name = sys.argv[1]
file_metadata = {'name': file_name}
media = MediaFileUpload('./'+file_name,
                        mimetype='text/plain')
file = drive_service.files().create(body=file_metadata,
                                    media_body=media,
                                    fields='id').execute()
