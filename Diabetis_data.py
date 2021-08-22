import pandas as pd

data = pd.read_csv('pima-indians-diabetes.csv')

print(data)

print(data.describe())
print(len(data))
data = {'Country':['INDIA', 'USA', 'INDIA', 'USA'],
        'year' :[2010, 2011, 2012, 2013],

        'Population':[20, 28, 32, 38]}

df = pd.DataFrame(data)
print(df)
print(df.Population.mean())
print(df.describe())

import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_column',None)
pd.set_option('display.width', 1200)


filename = "pima-indians-diabetes.csv"
h_names = ['preg', 'plasma', 'pres', 'skin', 'test', 'mass', 'bp', 'age', 'height']
df = pd.read_csv(filename, names=h_names)

print(df)
print(df.dtypes)

print(df.iloc[ 0 :20 , 0: ])

print(df.iloc[ : , [0,2,8]])

print(df.describe())

import pandas as pd
import numpy as np

# dictionary of lists
dict = {    'First Score': [100, 90, np.nan, 95],
            'Second Score': [30, 45, 56, np.nan],
            'Third Score': [np.nan, 40, 80, 98]
            }

#  Operation broadcasting

# creating a dataframe using dictionary
df = pd.DataFrame(dict)
print(df)


#using isnull() function
# bool_df=df.isnull()

# print(bool_df)
print('\n')

bool_df1 = df['First Score'].isnull()
bool_df1 = df['First Score'].isnull()


print(bool_df1)

