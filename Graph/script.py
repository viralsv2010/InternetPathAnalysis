#Reference from the http://stackoverflow.com/questions/24575869/read-file-and-plot-cdf-in-python

import numpy as np
import matplotlib.pyplot as plt

data_text_a = np.loadtxt('text/packet Loss/pair6a.txt')
data_text_b = np.loadtxt('text/packet Loss/pair6b.txt')
# Choose how many bins you want here
num_bins = 20

# Use the histogram function to bin the data
count, bin_edges = np.histogram(data_text_a, bins=num_bins, normed=True)
counts1, bin_edges1 = np.histogram(data_text_b, bins=num_bins, normed=True)

# Now find the cdf
cdf = np.cumsum(count)
cdf1 = np.cumsum(counts1)
# And finally plot the cdf
plt.plot(bin_edges[1:], cdf)
plt.plot(bin_edges1[1:], cdf1)
plt.show()