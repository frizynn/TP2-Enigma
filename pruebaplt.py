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

plt.show()