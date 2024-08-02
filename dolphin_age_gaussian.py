'''Histogram Plot'''

import numpy as np
import matplotlib.pyplot as plt


x = np.random.randn(1000000)*5 + 35
print(x)
print(type(x))
fig = plt.figure()
ax = fig.add_subplot(111)

# the histogram of the data

Nbins = 1000
ax.hist(x, Nbins)
# hist uses np.histogram under the hood to create 'n' and 'bins'.
# np.histogram returns the bin edges, so there will be Nbin probability
# density values (n), Nbin+1 bin edges (bins), and finally, Nbin patches.

plt.show()
