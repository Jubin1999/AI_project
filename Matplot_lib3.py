# Numbers with squared values

import matplotlib.pyplot as plt
x= [2, 3, 4, 5, 6, 7]
y = [4, 9, 16, 25, 36, 49]
#
plt.plot(x, y, marker='o', markerfacecolor='red', markersize=15,
          linestyle='dashed', color='blue')
#
plt.title("Numbers with squared values")
#
plt.xlabel('-------Numbers------->',   color='red')
plt.ylabel('-------Square------->',  color='blue')
#
plt.axis([1, 8, 2, 51])

plt.grid(True)
#
plt.annotate("This is the Square of 5 ", xytext=(3, 40), xy=(5, 25), arrowprops=dict(facecolor='black', shrink=.1))
plt.show()

