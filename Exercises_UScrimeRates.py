import pandas as pd
import numpy as np

crime = pd.read_csv("https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/04_Apply/US_Crime_Rates/US_Crime_Rates_1960_2014.csv")


# print(crime['Year'].dtype)

crime['Year']= pd.to_datetime(crime['Year'],format="%Y")

# print(crime['Year'].dtype)

crime.set_index('Year',inplace=True)

print(crime['Total'])

del crime['Total']

print(crime['Total'])