import numpy as np
import matplotlib

matplotlib.use('TkAgg')

import matplotlib.pyplot as plt


def default_function(input):
    if input > 0:
        return 1
    else:
        return 0

def relu(x):
    return np.maximum(0, x)

def step_function(x):
    return np.array(x > 0, dtype=np.int)

def sigmoid(x):
    return 1 / (1 + np.exp(-x))


X = np.arange(-5.0, 5.0, 0.1)
Y = sigmoid(X)
plt.plot(X, Y)
plt.ylim(-0.1, 5.5)

x = np.arange(-5.0, 5.0, 0.1)
y = relu(x)
plt.plot(x, y)
plt.ylim(-1.0, 5.5)


p = np.arange(-5.0, 5.0, 0.1)
q = step_function(x)
plt.plot(p, q)
plt.ylim(-1.0, 5.5)

plt.show()