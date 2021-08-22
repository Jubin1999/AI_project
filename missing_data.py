#Employees_with_missing_data.csv

import pandas as pd

# making data frame from csv file
data = pd.read_csv("Employees_with_missing_data.csv")
print(data)

# creating bool series True for NaN values

bool_series = data["Gender"].isnull()
#bool_series = data["First Name"].isnull()

print(bool_series)

# # # filtering data
# # # displaying data only with Gender = NaN
#
df2=data[0:11]["Gender"].fillna("No Gender")
print(df2)

