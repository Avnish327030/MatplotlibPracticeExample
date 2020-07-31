# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

print("Hello Matplotlib")

"""
Importing matplotlib.pyplot library
"""

import matplotlib.pyplot as plt
import numpy as np

# generating ndarry between o and 2 pi 
x=np.arange(0,np.math.pi*2,0.05)

y=np.sin(x)

plt.plot(x,y)

plt.xlabel("angle")
plt.ylabel("sine")
plt.title("Sin wave")
plt.show()


import pylab as pb
x=np.linspace(-3,3,30)
y=x**2
pb.plot(x,y,'k3')




pb.plot(x,np.sin(x),'g--')
pb.plot(x,np.cos(x),'r^')
pb.plot(x,-np.sin(x))

## creating empty  figure

fig=plt.figure()
 
# now addind axes to the figure

ax=fig.add_axes([0,0,1,2])

ax.set_xlabel("angle")
ax.set_ylabel("sine")
ax.set_title("sine wave")

x=np.arange(0,np.math.pi*2,0.05)
y=np.sin(x)
ax.plot(x,y)

help(fig.add_axes)
