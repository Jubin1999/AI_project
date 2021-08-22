#barh

import matplotlib.pyplot as plt
import numpy as np
langs = np.array (['C', 'C++', 'Java', 'Python', 'PHP'])
students = np.array ([23, 17,  35,   73,   12])
#
plt.barh(langs, students,  color='r', height = .5)
plt.show()