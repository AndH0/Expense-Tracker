import numpy as np
import matplotlib.pyplot as plt

x = [0, 1, 2, 3, 4, 5]
y = np.square(x)

plt.plot(x, y, label="kvadraticka")
plt.title("My first plot")
plt.xlabel("x(radians)")
plt.ylabel("sin(x)")
plt.legend()
plt.grid(True)
plt.show()


