import json

import gspread
import os
from oauth2client.service_account import ServiceAccountCredentials
import os.path


class GoogleSpreadSheets(object):

    scope = ['https://spreadsheets.google.com/feeds']
    gs_client_secret = {
        "type": os.getenv('GS_TYPE'),
        "project_id": os.getenv('GS_PROJECT_ID'),
        "private_key_id": os.getenv('GS_PRIVATE_KEY_ID'),
        "private_key": os.getenv('GS_PRIVATE_KEY', ''),
        "client_email": os.getenv('GS_CLIENT_EMAIL'),
        "client_id": os.getenv('GS_CLIENT_ID'),
        "auth_uri": os.getenv('GS_AUTH_URI'),
        "token_uri": os.getenv('GS_TOKEN_URI'),
        "auth_provider_x509_cert_url": os.getenv(
            'GS_AUTH_PROVIDER_X509_CERT_URL'),
        "client_x509_cert_url": os.getenv('GS_CLIENT_X509_CERT_URL')
    }

    BASE_DIR = os.path.dirname(os.path.realpath(__file__))

    def __init__(self, sheet_name="Untitled", worksheet_title="Sheet1"):
        # Use credentials to create a client to interact with the Google
        # Drive API
        # Check if client_secret.json file exists
        self.sheet_name = sheet_name
        self.worksheet_title = worksheet_title
        file_path = os.path.join(self.BASE_DIR, 'client_secret.json')
        if os.path.isfile(file_path):
            self.credentials = ServiceAccountCredentials\
                .from_json_keyfile_name(file_path, self.scope)
        else:
            self.gs_client_secret = json.dumps(self.gs_client_secret,
                                               indent=0).replace('\\n', u'n')
            self.gs_client_secret = json.loads(self.gs_client_secret)
            self.credentials = ServiceAccountCredentials\
                .from_json_keyfile_dict(self.gs_client_secret, self.scope)
        self.client = gspread.authorize(self.credentials)

        # Find a workbook by name and open the first sheet
        self.sheet = self.client.open(self.sheet_name).worksheet(
            self.worksheet_title)

    def append_row(self, data):
        rows_len = self.sheet.row_count
        self.sheet.insert_row(data, rows_len+1)

    def get_all_records(self, head=1):
        # Extract and print all of the values
        return self.sheet.get_all_records(head=head)


if __name__ == "__main__":
    spread_sheet = GoogleSpreadSheets("NSE Stocks", "DTK")
    print(spread_sheet.get_all_records())

a = [-8.73684211,
 -8.73684211,
 -8.73684211,
 -5.73684211,
 -5.73684211,
 -3.73684211,
 -3.73684211,
 -2.73684211,
  0.26315789,
  1.26315789,
  2.26315789,
  3.26315789,
  4.26315789,
  7.26315789,
  7.26315789,
  6.26315789,
  6.26315789,
  3.26315789,
  6.26315789]

b = [175, 175, 175, 178, 178, 180, 180, 181, 184, 185, 186, 187, 188, 191, 191, 190, 190, 187, 190]

min_diff_y = [-9.36842105,-9.36842105,-6.36842105,-6.36842105,-5.36842105,-4.36842105
,-3.36842105,-0.36842105,0.63157895,1.63157895,2.63157895,3.63157895
,4.63157895,6.63157895,5.63157895,2.63157895,5.63157895,5.63157895
, 5.63157895]