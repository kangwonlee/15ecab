import matplotlib.pyplot as plt
import numpy as np

x = np.arange(6)
y = np.arange(5)
z = x * y[:, np.newaxis]
while True:
    for i in xrange(5):
        if 0==i:
            p = plt.imshow(z)
            fig = plt.gcf()
            plt.clim()
            plt.title("Boring slide show")
        else:
            z = z + 2
            p.set_data(z)
        print ("step", i)
        plt.pause(0.5)
