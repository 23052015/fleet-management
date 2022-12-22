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


def menu():
    """
    Prints the menu and shows options to choose
    """

    while True:
        print("1. show all cars")
        print("2. Mark cars for sell, rent, service")
        print("3. Filter by model, category/plate/number/code/transmission")
        print("4. Update fleet")
        print("5. Exit")


        choice = int(input("Choose option: "))
        if choice == 1:
            show_all_cars()
            break
        elif choice == 2:
            mark_specific_cars()
            break
        elif choice == 3:
            filter_cars()
            break
        elif choice == 4:
            update()
            break
        else:
            print("Invalid choice. Choose 1-5")


def show_all_cars():
    print("All cars")



def mark_specific_cars():
    print("Specific cars")


def filter_cars():
    print("filter cars")


def update():
    print("update cars")


menu()



