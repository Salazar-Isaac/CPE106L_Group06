#Authors: Salazar, Isaac Joaquin D.
#         Joshua Rei Y.  Abundo
#         Clarrice  Ellyne  A.  Galang 
#         Christian Ray M. Factor 


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.dates as mdates
from tkinter import *

Data = pd.read_csv("https://covid.ourworldindata.org/data/owid-covid-data.csv")

class Function:
    
    def totalTested():
        Data.query('location=="Philippines" & date',inplace = True)

        df= pd.DataFrame(Data,columns=['location','date','total_tests'])

        last_element = df.iloc[-4]

        print("Total number of tested Filipinos as of",last_element.date, "in the", last_element.location, "=", last_element.total_tests, "Filipinos",)

        #Gui Calls

        newWin = Toplevel()
        newWin.title("Total Amount of People Tested in the Philippines")
        newWin.geometry("500x30")
        totalTestedText = Label(newWin, text = "Total number of tested Filipinos as of " + last_element.date + " in the " + last_element.location + " = ")
        noTotalTested = Label(newWin, text = last_element.total_tests)
        totalTestedText.grid(row=1, column=0)
        noTotalTested.grid(row=1, column=1)

    def totalCases():
        Data.query('location=="Philippines" & date',inplace = True)

        df= pd.DataFrame(Data,columns=['location','date','total_cases'])

        last_element = df.iloc[-1]

        print("Total cases as of",last_element.date, "in the", last_element.location, "=", last_element.total_cases, "Filipinos")

        #Gui Calls

        newWin = Toplevel()
        newWin.title("Total Cases in the Philippines")
        newWin.geometry("500x30")

        totalCasesText = Label(newWin, text = "Total cases as of " + last_element.date + " in the " + last_element.location + " = ")
        noTotalCases = Label(newWin, text = last_element.total_cases)
        totalCasesText.grid(row=0, column=0)
        noTotalCases.grid(row=0, column=1)

    def newestCases():
        Data.query('location=="Philippines" & date',inplace = True)

        df = pd.DataFrame(Data,columns=['location','date','new_cases'])

        last_element = df.iloc[-1]

        print("Total cases as of",last_element.date, "in the", last_element.location, "=", last_element.new_cases, "Filipinos")

        #Gui Calls

        newWin = Toplevel()
        newWin.title("Newest Cases in the Philippines")
        newWin.geometry("500x30")
        newCasesText = Label(newWin, text = "Newly added cases of Covid-19 as of  " + last_element.date + " in the " + last_element.location + " = ")
        newCases = Label(newWin, text = last_element.new_cases)
        newCasesText.grid(row=0, column=0)
        newCases.grid(row=0, column=1)

    def totalCasesPlot():
        Data.query('location=="Philippines" & date',inplace = True)
        df= pd.DataFrame(Data,columns=['location','date','total_cases'])
        last_element = df.iloc[-1]
        df.plot(x = 'date', y='total_cases', kind = 'scatter')
        plt.title("Number of Covid cases in the Philippines")
        plt.figtext(0.1, 0.0, "Total cases as of " + last_element.date + " in the " + last_element.location + " = ")
        plt.figtext(0.65, 0.0, last_element.total_cases)
        plt.show()
