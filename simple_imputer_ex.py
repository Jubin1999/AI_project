# import numpy as np
#
# # # Importing the SimpleImputer class
# from sklearn.impute import SimpleImputer
# #
# # # Imputer object using the mean strategy andmissing_values type for imputation
# imputer = SimpleImputer(missing_values = np.nan, strategy ='mean')
#
# # data =[ [12, np.nan, 34],
# #         [10, 32, np.nan],
# #         [np.nan, 11, 20]  ]
#
# data2 =np.array([ [12, np.nan, 34],
#         [10, 32, np.nan],
#         [np.nan, 11, 20]  ])
# #  list of lists
# print("Original Data : \n", data2)
# print("Numpy array Data : \n", data2)
#
# #Fitting the data to the imputer object
# imputer = imputer.fit(data2)
#
# # # Updating the origibnal data with imputed data
# data2 = imputer.transform(data2)
# print("Imputed Data : \n", data2)

import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
# data1=[["a",     "x"],
#       [np.nan,   "y"],
#       ["a",    np.nan],
#       ["b",      "y"]]
# # will through error with array of string
# data1=np.array([["a", "x"],
#       [np.nan, "y"],
#       ["a", np.nan],
#       ["b", "y"]])
#
data1 = pd.DataFrame([["a", "x"],
                   [np.nan, "y"],
                   ["a", np.nan],
                    ["b", "y"]])
print(data1)

imputer = SimpleImputer(missing_values = np.nan, strategy="most_frequent")
#imputer = SimpleImputer(missing_values = np.nan, strategy="constant", fill_value="2")

imputer = imputer.fit(data1)

data1 = imputer.transform(data1)
print(data1)
