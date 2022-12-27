# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import gspread
from google.oauth2.service_account import Credentials
import gspread_formatting
from gspread_formatting import *
import pandas as pd


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
        print("3. Filter code/n")
        print("4. Update fleet")
        print("5. Exit")

        choice = input("Choose option: ")
        if choice == '1':
            show_all_cars()

        elif choice == '2':
            print("Type plate number\n")
            find_specific_cars()

        elif choice == '3':
            print("Type the code: ")
            filter_cars()
            
        elif choice == '4':
            update_car_list()

        elif choice == '5':
            break    
        else:
            print("Invalid choice. Choose 1-5")
            
            
def show_all_cars():
    """
    Show all cars 
    """
    for dispo in disposition.range("A4:D25"):
        print(dispo.value)


def find_specific_cars():
    """
    Finds car based on plate-nr input 
    """
    plate_nr = input("")
    plate_nr_list = disposition.findall(plate_nr)
    # while True
    for plate_nr in plate_nr_list:
        if (plate_nr in plate_nr_list):
            print(f"Choose operation: Sell/Service/Rent for {plate_nr}\n")
            print("2.1 sell")
            print("2.2 rent")
            print("2.3 service")
            operation = input("Choose operation: ")
            if operation == "2.1":
                # format(plate_nr, {
                #     "backgroundColor": {
                #         "red": 5.5}})
                print("===> 2.1 selected")
                fmt = cellFormat(
                backgroundColor=color(1, 0.9, 0.9)
                 )

                format_cell_range(disposition, "A2", fmt)
               
        else:
            print("Invalid Choice, please try again")


def filter_cars():
    """
    Filter cars based on codes and display them
    """
    code = input("Type your code: ")
    code_list = disposition.findall(code)
    for code in code_list:
        if (code in code_list):
            print(f"This are the cars with code {code}")    


def update_car_list():
    """
    Updates cars in list 
    """
    new_car = input("") 
    disposition.append_rows(1)

  
menu()
