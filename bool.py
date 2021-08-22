import pandas as pd
#
data = {'name': ["Gaurav", "Ujjal", "Vivek", "Pankaj"],
        'degree': ["MBA", "BCA", "M.Tech", "MBA"],
        'score': [90, 40, 80, 98]}
# # default dataframe
df1 = pd.DataFrame(data)
# # creating the boolean series/array
bool_series=[True, False, True, False]
#
# # Boolean Indexing
df2 = pd.DataFrame(data, index =[bool_series] )
#
print(df1)
print("\n")
print(df2)
print("\n")
print(df2[bool_series])