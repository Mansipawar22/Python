import pandas as pd
import numpy as np
from io import StringIO,BytesIO

data = ('C1,C2,C3\n'
        'x,y,1\n'
        'a,b,2\n'
        'c,d,3')

print(data)     #it will give comma separated values
print(type(data))

#csv to dataframe conversion using StringIO
print(pd.read_csv(StringIO(data)))      #it will give dataframe

#read from specific columns
df=pd.read_csv(StringIO(data),usecols=['C1','C3'])
print('******',df)

#dataframe to csv
df.to_csv('ML_3.csv')

#Specifying col data types

data = ('a,b,c,d\n'
        '1,2,3,4\n'
        '5,6,7,8\n'
        '9,10,11,12')
print(data)

df=pd.read_csv(StringIO(data),dtype=float)
print(df)
print(type(df['a'][1]))   #str type

#different datatype for different col

df=pd.read_csv(StringIO(data),dtype={'b':int,'c':float,'a':'Int64'})
print(df)
print(df.dtypes)



data = ('index,a,b,c\n'
        '4,apple,bat,5.7\n'
        '8,orange,cow,10')

print(pd.read_csv(StringIO(data),index_col=2))          #try to chnage the 0 value witj 1,2 and 3 to see the difference

data = ('a,b,c\n'
        '4,apple,bat,\n'
        '8,orange,cow,')
print(pd.read_csv(StringIO(data)))   #it will consider 4 and 8 as index

print(pd.read_csv(StringIO(data),index_col=False))   #it will not consider anyhting as index

#combining usecols and index_col
print(pd.read_csv(StringIO(data),usecols=['b','c'],index_col=False))

#Quoting and escape characters. very useful in NLP
data = 'a,b\n"hello,\\"Mansi\\",nice to see you",5'
print(pd.read_csv(StringIO(data),escapechar='\\'))

