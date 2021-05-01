# Core Layer Version 2
# if code changes please tick version ++1
# Changes: made it print out last value of the dataframe

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.dates as mdates

Data = pd.read_csv("https://covid.ourworldindata.org/data/owid-covid-data.csv")

Data.query('location=="Philippines" & date',inplace = True)

df= pd.DataFrame(Data,columns=['location','date','total_cases'])


# df.plot(x = 'date', y='total_cases', kind = 'scatter')
# plt.title("Number of Covid cases in the Philippines")

# plt.show()

last_element = df.iloc[-1]
print(last_element.date)


print("Total cases as of",last_element.date, "in the", last_element.location, "=", last_element.total_cases)

OverflowError(status.update)
