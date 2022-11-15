import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()  # Create a figure containing a single axes ok.
ax.plot([1, 2, 3, 4], [1, 4, 2, 3]);  # Plot some data on the axes.pip
plt.show()

plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.show()