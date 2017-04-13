import numpy as np


def SimpleNN():
    x = np.array([1,2])
    w = np.array([[1,3,5],[2,4,6]])

    num = np.dot(x,w)

    return num

print(SimpleNN())
