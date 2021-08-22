
import matplotlib.pyplot as plt

x1 = [1, 2, 3]
y1 = [4, 5, 6]
x2 = [1, 3, 5]
y2 = [6, 5, 4]

plt.figure(1)
plt.plot(x1, y1)
plt.axis([0, 10, 0, 20])
plt.xlabel('MyX1')
plt.ylabel('MyY1')
plt.title(" First plot ")
plt.figure(2)
plt.plot(x2, y2)
plt.axis([0, 10, 0, 20])
plt.xlabel('MyX2')
plt.ylabel('MyY2')
plt.title("second plot")
plt.show()