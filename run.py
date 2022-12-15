# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import gspread
from google.oauth2.service_account import Credentials
import datetime 



SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Fleet')

disposition = SHEET.worksheet('disposition')
car = disposition.range()
date = datetime()


"""
def get_reservation_data():
    
    Get reservation duration and vehicule code
    
    print("Please enter the reservation period and vehicle code")
    print("Reservaion must have customer name and code 4 letters")
    print("Example: Johny Cage - 01.01.2022 FWAR")

    reservation_str = input("Enter your data here: ")
    

get_reservation_data()
"""
"""
def update_reservation_list():
    Receives a time span and type to be inserted in in the worksheet
    df["From"] = df["From"].dt.strftime("%Y-%m-%d %H:%M:%S.%f")
    df["To"] = df["To"].dt.strftime("%Y-%m-%d %H:%M:%S.%f")
    disposition.update([df.columns.values.tolist()] + df.values.tolist(), value_input_option='USER_ENTERED')


update_reservation_list()
"""