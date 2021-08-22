import pandas as pd
import numpy as np



dict = {    'First Score': [100, 90, np.nan, 95],
             'Second Score': [30, 45, 56, np.nan],
             'Third Score': [np.nan, 40, 80, 98]
            }



df = pd.DataFrame(dict)
print(df)



data=df.replace(to_replace=np.nan, value= -5)
 #data=df.replace(to_replace=np.nan, value= "Absent")
 #data=df.replace(to_replace=105, value= 10)

print(data)