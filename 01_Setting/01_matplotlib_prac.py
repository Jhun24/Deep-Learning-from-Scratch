import numpy as np
import matplotlib

matplotlib.use('TkAgg')

import matplotlib.pyplot as plt
from matplotlib.image import imread

img = imread("code.png")

plt.imshow(img)
plt.show()