import pandas as pd
import matplotlib.pyplot as plt


rawdata = pd.read_csv("dataset_majorcrime_centralcoast.csv")
filterChoice = None
crimelist = ["Murder", "Non-Domestic Assault", "Breaking and Entering Dwelling", "Robbery", "Attempted Murder", "Sexual Assault"]
visChoice = None


def display_rawdata():
    print("=== Displaying Raw Dataset ===\n=== Rates of different crime in the Central Coast ===\n")
    print(rawdata)
    input("Input any key to continue!")

def visualise_data():
    print("=== Data Visualiser ===")
    print()
    for i in crimelist:
        print(i)
    print("Back\n")
    visChoice = input("Please Choose a crime to visualise (1-7): ").strip()
    if visChoice == "1":
        rawdata.plot(kind="line",x='Year',y=['Murder'], color=['red'],alpha=1,title='Central Coast Murder Rates Over Years')
        plt.show()
    elif visChoice == "2":
        rawdata.plot(kind="line",x='Year',y=['Non-Domestic Assault'], color=['orange'],alpha=1,title='Central Coast Non-Domestic Assault Rates Over Years')
        plt.show()
    elif visChoice == "3":
        rawdata.plot(kind="line",x='Year',y=['Breaking and Entering Dwelling'], color=['purple'],alpha=1,title='Central Coast B.A.E Dwelling Rates Over Years')
        plt.show()
    elif visChoice == "4":
        rawdata.plot(kind="line",x='Year',y=['Robbery'], color=['blue'],alpha=1,title='Central Coast Robbery Rates Over Years')
        plt.show()
    elif visChoice == "5":
        rawdata.plot(kind="line",x='Year',y=['Attempted Murder'], color=['green'],alpha=1,title='Central Coast Attempted Murder Rates Over Years')
        plt.show()
    elif visChoice == "6":
        rawdata.plot(kind="line",x='Year',y=['Sexual Assault'], color=['yellow'],alpha=1,title='Central Coast Sexual Assault Rates Over Years')
        plt.show()
    elif visChoice == "7":
        print("Going Back!")
        pass
    else:
        print("Please choose a number from 1 to 7!")

def filter_data():
    print("=== Data Filtering ===")
    print("1. Filter Via Crime")
    print("2. Filter Via Timeframe")
    print("3. Back")
    filterChoice = input("=== Please Choose something to filter (1-3) ===\n Choose here: ").strip()
    if filterChoice == "1":
        print()
        for i in crimelist:
            print(f"Crime: {i}")
        print()
        crimeChoiceFiltering = input("Choose a crime to filter by (1-6): ")
        if crimeChoiceFiltering == "1":
            print(rawdata.loc[:,["Murder","Year"]])
            



    elif filterChoice == "2":
        pass





    elif filterChoice == "3":
        pass




    else:
        print("Please choose a number from 1 to 3!")