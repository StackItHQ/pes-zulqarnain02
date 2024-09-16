Superjoin Hiring Assignment🚀

## Overview
This project is designed to enable real-time synchronization between Google Sheets and a MySQL database. It uses Django as the web framework and integrates with Google Sheets API to automate the synchronization process. The system ensures that any changes made in Google Sheets are reflected in the database and vice versa.

##Technologies Used
-Django: Web framework for building the web application.
-MySQL: Database used for storing and managing data.
-Google Sheets API: Used to interact with Google Sheets for data synchronization.
-Webhooks: To handle real-time updates between the database and Google Sheets.
-Bootstrap: For styling the web pages.

## Features
1.Real-Time Synchronization: Detects changes in Google Sheets and updates the MySQL database accordingly. Similarly, changes in the database are reflected in Google Sheets.
2.CRUD Operations: Supports Create, Read, Update, and Delete operations for both Google Sheets and the database.
3.Dynamic Table Creation: Creates a new database table based on the structure of the Google Sheet if it does not exist.
4.Triggers and Webhooks: Uses MySQL triggers and webhooks to handle real-time synchronization.

## Project Setup
Prerequisites
-Python 3.8 or higher
-Django 5.1.1
-MySQL
-Google Cloud credentials for Sheets API

##Installation
1.Clone the Repository
   -git clone https://github.com/your-repo-url.git
   -cd your-repo-folder

2.Create a Virtual Environment
   -python -m venv env
   -source env/bin/activate  # On Windows use `env\Scripts\activate`
   
3.Install Dependencies
   -pip install -r requirements.txt
   
4.Configure Google Sheets API
   -Place your credentials.json file in the google_credentials directory.
   -Ensure the Google Sheets API is enabled in your Google Cloud project.
   
5.Update Settings
   -Edit settings.py to configure your MySQL database connection details.
   
6.Apply Migrations
   -python manage.py migrate
   
7.Run the Development Server
   -python manage.py runserver
   
## Usage
1.Sync Google Sheet
   -Navigate to http://localhost:8000/sync-google-sheet/.
   -Enter the Google Sheet ID and submit the form to synchronize the Google Sheet with the database.
   
2.Update Google Sheet
   -After synchronization, you can update the Google Sheet by clicking the "Update Database" button on the confirmation page.
   
## Files Overview
-google_sheet_sync_complete.html: Template displayed after successful synchronization with options to open the Google Sheet and update the database.
-sync_sheet.html: Form to enter the Google Sheet ID for synchronization.
-google_setting.py: Contains functions to authenticate and interact with Google Sheets API.
-google_sheet.py: Handles communication with the Google Sheets API, including fetching data from a Google Sheet and pushing updates to it.
-settings.py: Django settings file, including database configurations and Google Sheets credentials path.
-google_setting.py: Contains functions to authenticate and interact with Google Sheets API.
-credentials.json:
   -Purpose: Stores the OAuth 2.0 credentials required to authenticate with Google APIs.
   -Contents: Includes client_id, client_secret, and other necessary tokens for API access, generated via the Google Cloud Console.
-urls.py: URL configuration for the Django project, defining routes for synchronization and update operations.
-views.py: Contains the logic for synchronizing Google Sheets with the database, creating tables, and handling webhooks for real-time updates.

## Contributing
Feel free to fork the repository and submit pull requests for improvements or bug fixes. If you have any questions or issues, please open an issue on GitHub.
