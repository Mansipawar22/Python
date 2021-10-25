import pandas as pd
import numpy as np

df = pd.DataFrame(np.arange(0, 20).reshape(5, 4), index=['R1', 'R2', 'R3', 'R4', 'R5'],
                  columns=['C1', 'C2', 'C3', 'C4'])
df.head()
print(df)

df.to_csv('Test1.csv')

# Accessing the element
# 1. .loc   2.  .iloc

print(df.loc['R1'])
print(type(df.loc['R1']))

print(df.iloc[:,:])
print(type(df.iloc[:,:]))

print(df.iloc[0:3,0:2])
print(type(df.iloc[0:3,0:2]))

print(df.iloc[0:2,0:1])
print(type(df.iloc[0:2,0:1]))

print(df.iloc[0:2,0])
print(type(df.iloc[0:2,0]))

print(df.iloc[:,1:])
print(type(df.iloc[:,1:]))
print(df.iloc[:,1:].values)    #data frame to array conversion
print(df.iloc[:,1:].values.shape)

print(df.isnull().sum())
print(df['C1'].value_counts())

print(df['C1'].unique())

# Accessing elements without loc or iloc

print(df['C2'])
print(type(df['C2']))

print(df[['C1','C2']])

