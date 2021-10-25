import pandas as pd
import numpy as np
df=pd.read_csv('mercedesbenz.csv')
print(df.head())
print(type(df))

# print(df.info)
print(df.describe())   #gives data like mean median mode and other thingd

print(df['X0'].value_counts())   #to get the unique categories counted in a particalar col

print(df[df['y']>100])     #it will give us data for which the value of y is greater than 100 only