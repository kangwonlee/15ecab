"""
Demo of the fill function with a few features.

In addition to the basic fill plot, this demo shows a few optional feastures:

    * Multiple curves with a single command.
    * Setting the fill color.
    * Setting the opacity (alpha value).
"""
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 5.0, 100)
y1 = np.sin(x)
y2 = np.sin(3*x)
plt.fill(x, y1, 'b',
         x, y2, 'r',
         alpha=0.3)
plt.show()
