import pandas as pd

rawdata = pd.read_csv("dataset_majorcrime_centralcoast.csv")


def display_rawdata():
    print("=== Displaying Raw Dataset ===\n === Rates of different crime in the Central Coast ===")
    print(rawdata)

def filter_data(filterChoice):
    filterChoice = input("=== Please Choose something to print (1-4) ===")
    print("1. Filter Via Crime")
    print("2.Filter Via Timeframe")
