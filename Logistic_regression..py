# import pandas as pd
# import matplotlib.pyplot as plt
# from sklearn.linear_model import LogisticRegression
#
# def get_my_training_data(filename):
#     df = pd.read_csv(filename)
#     print(df)
#     x_data = []
#     y_data = []
#
#     for age_data, status in zip(df["Age"], df["Insured"]):
#         x_data.append([age_data])
#         y_data.append(status)
#     print("x=", x_data)
#     print("y=", y_data)
#     return x_data, y_data
#
# def logistic_model(x_parameters, y_parameters, question_value):
#     regr = LogisticRegression()
#     regr.fit(x_parameters, y_parameters)
#     print("Model parameters :")
#     print("Slope = ", regr.coef_)
#     print("Intercept = ", regr.intercept_)
#
#     status_of_policy = regr.predict([question_value])
#     print("status_of_policy: ", status_of_policy)
#     plt.scatter(x_parameters, y_parameters)
#     plt.show()
#
# def startAIAlgorithm():
#     x, y = get_my_training_data("Insurance_data.csv")
#     q_value = int(input("Enter valid age:  "))
#     logistic_model(x, y, q_value)
#
# if __name__=="__main__":
#     startAIAlgorithm()

import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression


def get_my_training_data(filename):
    df = pd.read_csv(filename)
    print(df)

    x_data = []
    y_data = []

    for age_data, status in zip(df["Age"], df["Insured"]):
        x_data.append([age_data])
        y_data.append(status)

    return x_data, y_data


def get_sigmoid(a):
    result = 1/(1+np.power(math.e, -a))
    return result


def logistic_model(x_parameters, y_parameters, question_value):
    # intantiating the class
    regr = LogisticRegression()
    regr.fit(x_parameters, y_parameters)        # calculate c (intercept) and m (slope)
    m = regr.coef_
    c = regr.intercept_
    print("Slope = ", m)
    print("Intercept = ", c)

    status_of_policy = regr.predict([[question_value]])
    if status_of_policy == 1:
        status_of_policy = "Yes"
    elif status_of_policy == 0:
        status_of_policy = "No"
    print("Status of policy is : ", status_of_policy)

    y_pred = regr.coef_ * x_parameters + regr.intercept_
    print("Y Predict = ", y_pred)
    plt.plot(x_parameters, get_sigmoid(y_pred), 'ro-')

    plt.scatter(x_parameters, y_parameters)
    plt.show()




def startAIAlgorithm():
    x, y = get_my_training_data("Insurance_data.csv")
    print("X = ", x)
    print("Y = ", y)

    q_value = int(input("Enter valid age: "))

    logistic_model(x, y, q_value)

if __name__ == '_main_':
    startAIAlgorithm()

