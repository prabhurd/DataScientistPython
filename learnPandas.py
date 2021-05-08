import pandas as pd
import numpy as np

list_nums = [0,1,2,3]

df_list = pd.DataFrame(list_nums)

df_list.columns = [ "COLUMN_"+str(i) for i in range(len(df_list.columns)) ]
df_list.index = ["ROW_"+str(i) for i in range(0,df_list.size)]

# print(df_list)
# print(50*'*')
#COLUMN Selection
# print(df_list['COLUMN_0'])

#COLUMN ADDITION
df_list['COLUMN_NEW'] = ['TEST'+str(i) for i in range(df_list.size)]
# print(df_list)

#COLUMN DEL

#del df_list['COLUMN_0']

# print(df_list)

#df_list.pop('COLUMN_NEW')

print(df_list)

print(40*'*')
#ROW SELECTION

#LOC
print(df_list.loc[:,:])
print(df_list.loc['ROW_0':'ROW_2',:])
print(df_list.loc[:'ROW_2',:])
print(df_list.loc['ROW_1':'ROW_2',:])
print(df_list.loc['ROW_1':'ROW_2','COLUMN_0':'COLUMN_NEW'])

#iLOC
print(df_list.iloc[:,:])
print(df_list.iloc[0:3,:])
print(df_list.iloc[:3,:])
print(df_list.iloc[1:3,:])
print(df_list.iloc[1:3,0:1])


print(df_list)

# df_list['COLUMN_SQUARE'] = df_list['COLUMN_0']*df_list['COLUMN_0']

df_list['COLUMN_SQUARE']  = df_list.loc[:,'COLUMN_0'] * df_list.loc[:,'COLUMN_0']

df_list.loc[:,'COLUMN_0'].apply(lambda x: x*x*x+8)

print(df_list)