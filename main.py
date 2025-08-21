import time
from data_module import (display_rawdata, filter_data, visualise_data)

def main_menu():
    while True:
        print("=== Central Coast Crime Rates ===\n=== Data Interface ===")
        print()
        print("1: View Dataset")
        print("2: View Graphic Visualisation")
        print("3: Filter Or Search")
        print("4: Close Program")
        print()
        MenuInput = input("Choose an option by inputting a number between 1 - 4.  ").strip()
        if MenuInput == "1":
            display_rawdata()
            print()
        elif MenuInput == "2":
            visualise_data()
            print()
        elif MenuInput == "3":
            print()
            filter_data()
            print()
        elif MenuInput == "4":
            print("bye bye see you next time")
            break
        else:
            print("Invalid digit, please put a number from 1 - 4.")
            input("Input any key to continue!")
            print()

if __name__ == "__main__":
    main_menu()