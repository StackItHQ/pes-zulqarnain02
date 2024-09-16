import os
import google.auth.exceptions
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from . import settings
# Define the path to your credentials JSON file
CREDENTIALS_FILE = os.path.join(os.path.dirname(__file__), 'google_credentials', 'credentials.json')

# Define the Google Sheets API scopes
SCOPES = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']

def get_google_sheets_service():
    """Load credentials and return a Google Sheets API service."""
    creds = None
    token_path = os.path.join(os.path.dirname(__file__), 'google_credentials', 'token.json')

    # Check if token.json exists, which stores the user's credentials
    if os.path.exists(token_path):
        creds = Credentials.from_authorized_user_file(token_path, SCOPES)
    
    # If credentials are invalid or do not exist, request user authorization
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
              settings.GOOGLE_SHEETS_CREDENTIALS_PATH, 
              SCOPES
            )
        creds = flow.run_local_server(port=8000)
        
        # Save the credentials for the next run
        with open(token_path, 'w') as token:
            token.write(creds.to_json())
    
    # Build the service for Google Sheets
    service = build('sheets', 'v4', credentials=creds)
    return service
