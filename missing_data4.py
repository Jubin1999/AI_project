import pandas as pd
import numpy as np
# dictionary of lists
dict = {    'First Score': [100, 90, np.nan, 95],
            'Second Score': [30, 45, 56, np.nan],
            'Third Score': [np.nan, 40, 80, 98]
            }


# creating a dataframe using dictionary
df = pd.DataFrame(dict)
print(df)
#data=df.interpolate(method="linear", limit_direction="forward")
#data=df.interpolate(method="linear", limit_direction="backward")
data=df.dropna()
print(data)