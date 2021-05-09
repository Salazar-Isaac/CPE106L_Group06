# Core Layer Version 2
# if code changes please tick version ++1
# Changes: made it print out last value of the dataframe

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.dates as mdates

Data = pd.read_csv("https://covid.ourworldindata.org/data/owid-covid-data.csv")


def TotalTested():
    Data.query('location=="Philippines" & date',inplace = True)

    df= pd.DataFrame(Data,columns=['location','date','total_tests'])

    last_element = df.iloc[-3]

    print("Total number of tested Filipinos as of",last_element.date, "in the", last_element.location, "=", last_element.total_tests, "Filipinos")



def TotalCases():
    Data.query('location=="Philippines" & date',inplace = True)

    df= pd.DataFrame(Data,columns=['location','date','total_cases'])

    last_element = df.iloc[-1]

    print("Total cases as of",last_element.date, "in the", last_element.location, "=", last_element.total_cases, "Filipinos")

def NewestCases():
    Data.query('location=="Philippines" & date',inplace = True)

    df= pd.DataFrame(Data,columns=['location','date','new_cases'])

    last_element = df.iloc[-1]

    print("Total cases as of",last_element.date, "in the", last_element.location, "=", last_element.new_cases, "Filipinos")

TotalCases()

TotalTested()

NewestCases()