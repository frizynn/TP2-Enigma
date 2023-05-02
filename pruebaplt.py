from matplotlib import pyplot as plt

import matplotlib.pyplot as plt
import numpy as np

# First plot
plt.subplot(1,2,1)  # 1 row, 2 columns, first plot
x1 = np.arange(0, 10, 0.1)
y1 = np.sin(x1)
plt.plot(x1, y1)
plt.title('Plot 1')

# Second plot
plt.subplot(1,2,2)  # 1 row, 2 columns, second plot
x2 = np.arange(0, 10, 0.1)
y2 = np.cos(x2)
plt.plot(x2, y2)
plt.title('Plot 2')

plt.axhline(y=0.5, color='g', linestyle=':', linewidth=3)
plt.show()

plt.show()

ENGLISH_LETTERS_FRECUENCIES = {
    "a": 0.08167, "b": 0.01492, "c": 0.02782, "d": 0.04253, "e": 0.12702, "f": 0.02228,
    "g": 0.02015, "h": 0.06094, "i": 0.06966, "j": 0.00153, "k": 0.00772, "l": 0.04025,
    "m": 0.02406, "n": 0.06749, "o": 0.07507, "p": 0.01929, "q": 0.00095, "r": 0.05987,
    "s": 0.06327, "t": 0.09056, "u": 0.02758, "v": 0.00978, "w": 0.02360, "x": 0.00150,
    "y": 0.01974, "z": 0.00075
}

l_x = []
l_y = []
for x, y in ENGLISH_LETTERS_FRECUENCIES.items():
    l_x.append(x)
    l_y.append(y)

promedio = sum(l_y) / len(l_y)
print(promedio)