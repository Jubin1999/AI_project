import pandas as pd

#s = pd.Series([9, 8, 7, 5, 1, 0, 5, 7, 100])
#print(s)

s = pd.Series([9, 8, 7, 6], index = ['#', '$', '%', '^'])
print(s)
print(s[['^', '$']])