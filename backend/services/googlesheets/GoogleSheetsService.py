from __future__ import print_function
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# The ID and range of a sample spreadsheet.
INPUT_SPREADSHEET_ID = '1ZplElpGuBVlnkSquSuGDLiD6L8c27O20C0KEQn5K0pc'
INPUT_RANGE_NAME = 'Input!A1:A100'
SINGLE_OUTPUT_SPREADSHEET_ID = '1pCI31UUBQtMJiH2mAqjeC3siE0Pks3yu1xRupS8a9QY'
HISTORICAL_OUTPUT_SPREADSHEET_ID = '1hq-i4YKAGv7HvirtjqL-8TNOH0RPHXUTqyFy8oOLSFE'


def google_authorize():
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('sheets', 'v4', credentials=creds)

        # Call the Sheets API
        sheet = service.spreadsheets()
        return sheet
    except HttpError as err:
        print(err)


class GoogleSheetsService:
    def get_video_ids_from_google_sheets(self):
        sheet = google_authorize()
        result = sheet.values().get(spreadsheetId=INPUT_SPREADSHEET_ID,
                                    range=INPUT_RANGE_NAME).execute()
        values = result.get('values', [])

        if not values:
            print('No data found.')
            return

        print('Name, Major:')
        i = 0
        video_ids = []
        for row in values:
            # Print video ids from Google sheet
            i += 1
            print(f'index {i} videoId {row[0]}')
            video_ids.append(row[0])
        print(f'Got {i} videoIds from google sheet')
        return video_ids

    def add_row(self, model, tab_range, spread_sheet_id):
        print(f"Add row triggered with input: {model}")
        sheet = google_authorize()
        try:
            # How the input data should be interpreted.
            value_input_option = 'USER_ENTERED'
            # How the input data should be inserted.
            insert_data_option = 'INSERT_ROWS'
            value_range_body = {
                "values": model
            }

            request = sheet.values().append(spreadsheetId=spread_sheet_id, range=tab_range,
                                            valueInputOption=value_input_option,
                                            insertDataOption=insert_data_option, body=value_range_body)
            response = request.execute()
        except Exception as ex:
            print("Exception while uploading a row:"+ex)
        print("upload a row in spreadsheet:"+spread_sheet_id)

    # def upload_data_to_youtube_historical_spreadsheet(self):
    #     pass

    def empyt_sheet(self):
        sheet = google_authorize()
        range_ = 'output!A2:Z1000'
        clear_values_request_body = {}
        request = sheet.values().clear(spreadsheetId=SINGLE_OUTPUT_SPREADSHEET_ID, range=range_,
                                       body=clear_values_request_body)
        response = request.execute()
        print(f'response from empty sheets method. ${response}')
        return "Done! No Values at Output Sheets"
