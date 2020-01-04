#!/usr/bin/python3
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.cloud import translate_v2

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# The ID and range of the spreadsheet.
SPREADSHEET_ID = '1BWzfR4BuTKvrAZxqAlBzT4hrhOgXRCK_e38XQhlB8AI'
READ_RANGE = 'Translation!A1:A200'
WRITE_RANGE = 'Translation!B1:B200'

def translate(values):
    '''
    Takes in a list of values to translate. Joins them into
    one string using the ** delimeter to reduce network traffic
    Splits the resulting translated text back into a list.
    '''
    translate_client = translate_v2.Client()
    text = '**'.join(values)
    result = translate_client.translate(text, target_language="zh")

    return result['translatedText'].split("**")


def main():
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                                range=READ_RANGE, majorDimension="COLUMNS").execute()
    values = result.get('values', [])


    # Transformation
    translated = translate(values[0])

    # Writing to sheet       
    write_body = {
        'values': [translated], # Put into another list since required in [[vals]] format
        'majorDimension': "COLUMNS",
    }

    write_result = sheet.values().update(spreadsheetId=SPREADSHEET_ID, range=WRITE_RANGE,
                                        valueInputOption="RAW",body=write_body).execute()


if __name__ == '__main__':
    main()