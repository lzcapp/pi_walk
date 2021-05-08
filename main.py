# Python code for 2D random walk.

import matplotlib as mpl
import numpy
import pylab

mpl.rcParams['agg.path.chunksize'] = 10000

filename = input("Enter data file's name (no .txt extension): ")

with open("data/" + filename + ".txt", "r", encoding='utf8') as f:
    data = f.read()
    # data = re.sub("[\x16]", '"', f.read())

n = len(data)

# creating two array for containing x and y coordinate
# of size equals to the number of size and filled up with 0's
x = numpy.zeros(n)
y = numpy.zeros(n)

# filling the coordinates with random variables
for i in range(3, n):
    val = data[i]
    if val == "0" or val == "1":
        x[i] = x[i - 1]
        y[i] = y[i - 1] + 1
    elif val == "2" or val == "3":
        x[i] = x[i - 1] + 1
        y[i] = y[i - 1] + 1
    elif val == "4" or val == "5":
        x[i] = x[i - 1] + 1
        y[i] = y[i - 1]
    elif val == "6" or val == "7":
        x[i] = x[i - 1] + 1
        y[i] = y[i - 1] - 1
    elif val == "8" or val == "9":
        x[i] = x[i - 1]
        y[i] = y[i - 1] - 1
    elif val == "a" or val == "b":
        x[i] = x[i - 1] - 1
        y[i] = y[i - 1] - 1
    elif val == "c" or val == "d":
        x[i] = x[i - 1] - 1
        y[i] = y[i - 1]
    elif val == "e" or val == "f":
        x[i] = x[i - 1] - 1
        y[i] = y[i - 1] + 1
    else:
        x[i] = x[i - 1]
        y[i] = y[i - 1]

# plotting stuff:
pylab.title("Random Walk [" + filename + "] (n = 10^9 digits)")
pylab.plot(x, y, linewidth=0.01)
pylab.savefig("output/" + filename + ".png", bbox_inches="tight", dpi=3600)
pylab.show()
