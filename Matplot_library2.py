import numpy as np
import matplotlib.pyplot as plt

time_step = 0.02
period = 5.
time_vect = np.arange(0, 20, time_step)

sig = np.sin(2 * np.pi / period * time_vect) + 0.5 *np.random.random(time_vect.size)
plt.plot(sig)
print("The signal size is: ", sig.size)
plt.show()


