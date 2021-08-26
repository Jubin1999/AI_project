import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression


def get_my_training_data(filename):
    df = pd.read_csv(filename)
    print(df)
    x_data = []
    y_data = []

    for s_f, f, b_rm, bt_rm, price in zip(df["square_feet"], df["floors"], df["bedrooms"], df["bathrooms"],df["price"]):
        x_data.append([s_f, f, b_rm, bt_rm])
        y_data.append(price)
    print("x=", x_data)
    print("y=", y_data)
    return x_data, y_data


def liner_model(x_parameters, y_parameters,question_value):
    #intantiating the class
    regr = LinearRegression()
    regr.fit(x_parameters, y_parameters)
    print("Model Parameters :")
    print("Slope = ", regr.coef_)
    print("Intercept = ", regr.intercept_)
    predicted_price = regr.predict([question_value])
    all_predicted_price = regr.predict(x_parameters)
    print("Predicted price is ", predicted_price)



def startAIAlgorithim():
    x,y = get_my_training_data("House_price_data_3_colm.csv")
    x_value1 = int(input("Enter the square_feet: "))
    x_value2 = int(input("Enter floors: "))
    x_value3 = int(input("Enter no.of bedrooms: "))
    x_value4 = int(input("Enter no. of bathrooms: "))
    print("\n")
    x_value = [x_value1, x_value2, x_value3, x_value4]
    liner_model(x,y,x_value)

if __name__=="__main__":
      startAIAlgorithim()