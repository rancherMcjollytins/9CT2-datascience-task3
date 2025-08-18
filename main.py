import time
from data_module import (display_rawdata, filter_data,)

def main_menu():
    while True:
        print("=== Central Coast Crime Rates ===\n=== Data User Visualiser ===")
        print()
        print("1: View Dataset")
        print("2: View Graphic Visualisation")
        print("3: Filter Or Search")
        print("4: Close Program")
        print()
        MenuInput = input("Choose an option by inputting a number between 1 - 4.  ")
        if MenuInput == "1":
            display_rawdata()
            print()
            time.sleep(1)
        elif MenuInput == "2":
            print("imagine a cool graph and stuff here")
            print()
            time.sleep(1)
        elif MenuInput == "3":
            filter_data()
            print()
            time.sleep(1)
        elif MenuInput == "4":
            print("bye bye see you next time")
            break
        else:
            print("Invalid digit, please put a number from 1 - 4.")
            print()
            time.sleep(1)

if __name__ == "main":
    main_menu()