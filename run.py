# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import gspread
from google.oauth2.service_account import Credentials

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
code = disposition.col_values(3)

cell_list = disposition.findall("2022")
print(cell_list)

def get_reservation_data():
    """
    Get reservation duration and vehicule code
    """
    print("Please enter the reservation period and vehicle code")
    print("Reservaion must have customer name and code 4 letters")
    print("Example: 25.12.2022 - 01.01.2022 FWAR")

    reservation_str = input("Enter your data here: ")
    

get_reservation_data()
