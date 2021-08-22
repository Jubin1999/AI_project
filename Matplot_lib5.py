#pie chart

import matplotlib.pyplot as plt

langs    = ['C', 'C++', 'Java', 'Python', 'PHP']
students = [23,  17,  35,  73,  12]

plt.pie(students, labels = langs)
plt.show()