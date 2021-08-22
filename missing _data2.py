import pandas as pd
import numpy as np

# dictionary of lists
dict = {    'First Score': [100, 90, 105, 95],
            'Second Score': [30, 45, 56, 105],
            'Third Score': [105, 40, 80, 98]
            }

#  Operation broadcasting

# creating a dataframe using dictionary
df = pd.DataFrame(dict)
print(df)

# fill the Not Available data with some vale

data = df.replace(to_replace=105, value= 10)
#data = df.replace(to_replace=np.nan, value= "Absent")
print(data)


# print("\n")
# df4=df.fillna(method="bfill")
# print(df4)