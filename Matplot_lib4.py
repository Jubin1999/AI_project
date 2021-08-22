import matplotlib.pyplot as plt

langs    = ['C', 'C++', 'Java', 'Python', 'PHP']
students = [23,   17,    35,      73,      12]

plt.bar(langs, students,  color='b' ,width = 0.3)
plt.show()
