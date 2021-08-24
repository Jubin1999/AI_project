# import pandas as pd
# import matplotlib.pyplot as plt
# #from skelearn.linear_model import LinearRegression
#
#
#
# def startAIAlgorithm():
#     df = pd.read_csv("House_price.csv")
#     print(df)
#     x_data = []
#     y_data = []
#
#     for square_feet_data, price_data in zip(df["square_feet"],df["price"]):
#         x_data.append([square_feet_data])
#         y_data.append([price_data])
#
#     print("x = ", x_data)
#     print("Y = ", y_data)
#
#
# if __name__=="__main__":
#     startAIAlgorithm()

# import pandas as pd
# import matplotlib.pyplot as plt
# from sklearn.linear_model import LinearRegression
#
#
# def get_my_training_data("House_price.csv"):
#      df = pd.read_csv("House_price.csv")
#      print(df)
#
#      x_data = []
#      y_data = []
#
#      for x_data, y_data in zip(df["square_feet"], df["price"]):
#         x_data.append([i])
#         y_data.append([j])
#
#     return x_data, y_data
# def linear_model(x_parameters, y_parameters, question_value):
#     regr = LinearRegression()
#     regr.fit(x_parameters, y_parameters)        # calculate c (intercept) and m (slope)
#     m = regr.coef_
#     c = regr.intercept_
#     print("Slope = ", m)
#     print("Intercept = ", c)
#
#     predicted_price = regr.predict([[question_value]])
#     print("Predicted price is : ", predicted_price)
#
#     allPredictedPrice = regr.predict(x_parameters)
#
#     plt.scatter(x_parameters, y_parameters, color = "y")
#
#     plt.scatter(x_parameters, y_parameters, color = "r")
#     plt.plot(x_parameters, allPredictedPrice, color = "b")
#
#     plt.scatter(question_value, predicted_price, color = "k", marker = "*")
#
#     plt.show()
#
#     def startAIAlgorithm():
#         x, y = get_my_training_data("House_price.csv")
#         # print("X = ", x)
#         # print("Y = ", y)
#
#         q_value = int(input("Enter the square feet value: "))
#
#         linear_model(x, y, q_value)
#
#     if __name__ == '__main__':
#         startAIAlgorithm()

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

def get_my_training_data(filename):
    df = pd.read_csv(filename)
    x_data = []
    y_data = []

    for square_feet_data, price_data in zip(df["square_feet"], df["price"]):
        x_data.append([square_feet_data])
        y_data.append([price_data])

    return x_data, y_data



def linear_model(x_parameters, y_parameters, question_value ):
    # intantiating the class
    regr = LinearRegression()
    regr.fit(x_parameters, y_parameters)  # calculate the c or( intercept) , m or slope
    m=regr.coef_
    c= regr.intercept_
    print("Slope  = ", m)
    print("Intercept = ", c)

    predicted_price = regr.predict([[question_value]])
    print("Predicted price is : ", predicted_price)

    allPredictedPrice = regr.predict(x_parameters)

    plt.scatter(x_parameters, y_parameters, color = "y")

    plt.scatter(x_parameters, y_parameters, color = "r")
    plt.plot(x_parameters, allPredictedPrice, color = "b")

    plt.scatter(question_value, predicted_price, color = "k", marker = "*")

    plt.show()

    x_input = int(input("Enter the questioned data ="))
    y_predict = c + m * x_input
    print(y_predict)


def startAIAlgorithm():
    x, y = get_my_training_data("House_price.csv")
    print("x = ",x)
    print("y= ",y)
    q_value= 700
    linear_model(x, y, q_value)


if __name__=="__main__":
      startAIAlgorithm()


