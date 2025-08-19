import pandas as pd
import matplotlib.pyplot as plt


rawdata = pd.read_csv("dataset_majorcrime_centralcoast.csv")
filterChoice = None
rawdata.iloc[0:6 ,0]



def display_rawdata():
    print("=== Displaying Raw Dataset ===\n === Rates of different crime in the Central Coast ===")
    print(rawdata)

def visualise_data():
    print("Visualising!!!")
    rawdata.plot(kind="line",x='Year',y=['Murder'], color=['red'],alpha=1,title='Central Coast Murder Rates Over Years')
    plt.show()

def filter_data():
    print("=== Data Filtering ===")
    print("1. Filter Via Crime")
    print("2. Filter Via Timeframe")
    print("3. Back")
    filterChoice = input("=== Please Choose something to filter (1-3) ===\n Choose here: ").strip()
    if filterChoice == "1":
        print("choose crime")
        print(rawdata.iloc[0,0:5])
    elif filterChoice == "2":
        pass
    elif filterChoice == "3":
        pass
    else:
        print("Please choose a number from 1 to 3!")