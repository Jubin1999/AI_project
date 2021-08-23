# import matplotlib.pyplot as plt
# import numpy as np
#
# def estimate_my_coef(x,y):
#     n = np.size(x)
#     m_x = np.mean(x)
#     m_y = np.mean(y)
#     sum_xy = np.sum(x*y)
#     sum_xx = np.sum(x*x)
#
#     SS_xy = sum_xy - m_x * m_y * n
#     SS_xx = sum_xx - m_x * m_x * n
#
#     m = SS_xy / SS_xx
#     c = m_y - m * m_x
#     return(m, c)
#
#
#
# def startAIAlgorithm():
#     x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
#     y = np.array([1, 2, 3, 4, 5, 6, 7, 6, 9, 10])
#     m, c = estimate_my_coef(x, y)
#     print('Slope m = ', m)
#     print("Intercept c=", c)
#     print("Model : y = ", m, " *x + ", c)
#     plt.scatter(x, y, color = "r", maker ="0", s=30)
#     plt.show()
#
#
#
#
# if __name__=="__main__":
#     startAIAlgorithm()
#
#
import numpy as np
import matplotlib.pyplot as plt

def estimate_my_coef(x,y):
    n=np.size(x)
    #mean of x and y
    m_x=np.mean(x)
    m_y = np.mean(y)
    sum_xy = np.sum(x*y)
    sum_xx = np.sum(x * x)

    SS_xy = sum_xy - m_x * m_y * n
    SS_xx = sum_xx - m_x * m_x * n
    #calculate regression coefficient

    m = SS_xy / SS_xx
    c = m_y - m * m_x
    return( m, c)

def plot_regression_line(x,y,b):

    plt.scatter(x, y , color = "r", marker ="o", s=30)  # original data plot

    y_predict = b[0]  + b[1]* x

    plt.scatter(x, y_predict, color="g", marker="o", s=30)  # predicted values scatter plot

    plt.plot(x, y_predict, color= "b")

    plt.show()

def startAIAlgorithm():
    x = np.array([0,1,2,3,4,5,6,7,8,9])
    y = np.array([1,3,2,5,7,8,8,9,10,12])
    #Estimation the coefficients  bo, b1
    m, c =estimate_my_coef(x,y)
    m=m
    c=c
    print('Slope m = ', m)
    print("Intercept c=", c)
    print("Model :  y =  ",  m, " * x  + ", c)
    plot_regression_line(x,y, [c, m])

    x_input= int(input("Enter the questioned data =" ))
    y_predict= c +  m * x_input
    print(y_predict)

if __name__=="__main__":
    startAIAlgorithm()

