import numpy as np

x = np.array([[51,55],[14,19],[0,4]])

x = x.flatten()
print(x)

print(x[np.array([0,2,4])])

print(x[x>15])