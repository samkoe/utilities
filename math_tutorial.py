# math_tutorial.py

import matplotlib.pyplot as plt
import numpy as np

'''
# Multiplication vs. Exponentiation

x = np.arange(-10, 10, 1)

plt.plot(x, x * 2, 'r^', label="x * 2")
plt.plot(x, x ** 2, 'bo', label="x ** 2")

plt.legend()
plt.show()

'''
# sin(x) / x vs. cos(x)

def f(x):
    return np.sin(x) / x

def g(x):
    return np.cos(x)

x = np.arange(-15.0, 15.0, 0.1)

plt.plot(x, f(x), 'r', label="sin(x)/x")
plt.plot(x, g(x), 'b', label="cos(x)")

plt.legend()
plt.show()