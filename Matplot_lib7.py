import matplotlib.pyplot as plt

x1 = [1, 2, 3, 4, 5, 6, 7]
y1 = [9, 12, 9, 16, 20, 36, 30]

x2 = [2, 3, 4, 5, 6, 7]
y2 = [4, 15, 6, 10, 15, 19]

plt.bar(x1, y1, label = "1st dataset", color='b')
plt.bar(x2, y2, label = "2nd dataset", color='r')

plt.plot(x1, y1, x2, y2)
plt.title("bar chart")
plt.xlabel('X data', color='red')
plt.ylabel('Y data', color='blue')
plt.legend()
plt.show()