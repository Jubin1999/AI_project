import matplotlib.pyplot as plt
x1=  [1,   3,  5,  7,  9, 11, 13]
y1 = [9, 12, 9, 16, 20, 36, 30]
#
x2=      [2, 4, 6, 8, 10, 12, 14]
y2 =     [3, 4, 15, 6, 10,  15, 19]
plt.bar(x1, y1, label=" 1st dataset",  color='b')
plt.bar(x2, y2, label=" 2nd dataset",  color='g')
plt.plot(x1, y1, x2, y2)
plt.title("bar chart ")
plt.xlabel('X data',   color='red')
plt.ylabel('Y data',  color='green')
plt.legend()
plt.show()