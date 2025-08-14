import pandas as pd

rawdata = pd.read_csv("dataset_majorcrime_centralcoast.csv")

def display_rawdata():
    print("Displaying Raw Dataset!")
    print(rawdata)