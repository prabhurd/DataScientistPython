#https://nbviewer.jupyter.org/github/justmarkham/pandas-videos/blob/master/pandas.ipynb#1.-What-is-pandas%3F-%28video%29

import pandas as pd
import numpy as np

'''1. What is pandas?'''

'''2. How do I read a tabular data file into pandas? '''

df = pd.read_table('test.txt',sep=" ")
# print(df.columns)

'''How do I select a pandas Series from a DataFrame?'''
# print(df['FirstName'])


'''
Why do some pandas commands end with parentheses (and others don't)?
'''
print(df.head(2))

print(df.shape)

'''
How do I rename columns in a pandas DataFrame?
'''

df['CityName'] = df['City'].str.upper()

del df['City']

print(df)