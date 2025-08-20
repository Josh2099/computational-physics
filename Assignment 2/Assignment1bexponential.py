#Code for exponential distribution
#Name: Joshna Anna Sam, Roll no: 2311077

import matplotlib.pyplot as plt
import Joshnalib
import numpy as np


xval,yval=Joshnalib.LCG(x=0.1,c=12345,a=1103515245,m=32768,N=5000,k=5)
m=32768
y=[]
for i in xval:
    y.append(-(np.log(i))/(float(m)))

plt.hist(y, bins=40, color="skyblue", edgecolor="black")
plt.ylabel("Frequency")
plt.xlabel("Values")
plt.title("HISTOGRAM")
plt.savefig("Histogram.png")

# Display the plot
plt.show()

