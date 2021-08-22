import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

population = np.random.rand(100)
area = np.random.randint(100,600,100)

continent = ['north america', 'europe', 'asia','australia']*25

df = pd.DataFrame(dict(population = population, area = area, continent = continent))

figure, axis = plt.subplots()
col = {'north america':'red', 'europe':'green', 'asia':'blue', 'australia':'black'}
axis.scatter(df['population'], df['area'], c=df['continent'].map(col))
plt.show()