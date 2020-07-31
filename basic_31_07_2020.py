# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 07:41:29 2020

@author: avnyadav
"""
"""
Importing matplotlib.pyplot module to work with graphs
"""

import matplotlib.pyplot as plt

"""
matplotbil.figure module contain figure class and it is top level contain for all  plot 
element. The figure element is instantiated by calling figure() function from
pyplot module.
"""
HEIGHT=10
WIDTH=20

fig=plt.figure(figsize=(WIDTH,HEIGHT),dpi=10,facecolor="green",edgecolor="red",linewidth=20)

"""
Matplotlib  Axes class 

Axes object is the region of image with data space. A given figure can contain many axes but

Axes can be related with only one figure at a time.
[0,0,1,1,]
[left,bottom,width,height]
"""

ax=fig.add_axes([0,0,1,1])

y = [1, 4, 9, 16, 25,36,49, 64]
x1 = [1, 16, 30, 42,55, 68, 77,88]
x2 = [1,6,12,18,28, 40, 52, 65]


## creating figure
fig=plt.figure()

# creating axes to plot data

ax=fig.add_axes([0,0,1,1])

l1=ax.plot(x1,y,"gs-") # greeen color square marker and solid line
l2=ax.plot(x2,y,"bH--") # blue color Hexagonal marrker and -- line

ax.legend(labels=('tv','Smartphone'),loc="upper right") #adding legends to upper right
ax.set_title("Advertisement on sale")
ax.set_xlabel("X axis")
ax.set_ylabel("Y axis")
plt.show()


plt.plot([1,2,3])

"""
subplot function allow us to create muliplt axes in fig. it tooks 3 number as parameter where 
first number belongs to rows and second number belongs to column and 3 number lebongs to index

"""
plt.subplot(211)  #it will plot graph in 2 row 1 column at index position 1
plt.plot(range(12))

plt.subplot(212,facecolor="y") #it will plot graph in 2 row 1 column index position 2
plt.plot(range(12))

"""
if we use subplot and new index position overlap with other suplot then it will overwrite old one.


But we have add_subplot method on figure which allow us to define an graph without overwrite old one,
"""


fig=plt.figure()  
ax1=fig.add_subplot(111,facecolor="y") ## creating sublot
ax1.plot([1,2,3])
ax2=fig.add_subplot(221,facecolor="m")  ## creataing other subplpot with the help of add_subplot method.
ax2.plot(range(12))


import numpy as np

X=np.arange(0,np.math.pi*2,0.05)
y=np.sin(X)

fig=plt.figure()
ax1=plt.subplot(111)  ## created a subplot

ax1.plot(X,y)

ax2=fig.add_subplot(222)  ## added another subplot within above subplpot
ax2.plot(X,np.cos(X))

ax1.set_xlabel("angle")
ax1.set_ylabel("sine")
ax2.set_xlabel("angle")
ax2.set_ylabel("cose")

ax1.set_title("Sin Wave")
ax2.set_title("Cos Ware")
plt.show()

"""
Subplots function return 2 dimension axes as specified in paramenter.
we can use axes like 2d array.
"""

fig,a=plt.subplots(2,2)  ## created 4 axes 2X2

x=np.arange(1,5)

##accessing axes like 2d array.
a[0][0].plot(x,x**2)
a[0][0].set_title("Square")

a[0][1].plot(x,x**3)
a[0][1].set_title("Cubic")

a[1][0].plot(x,np.log10(x))
a[1][0].set_title("Log 10")

a[1][1].plot(x,np.exp(x))
a[1][1].set_title("Exponential")

plt.show()



## subplot2grid function allow us to create axis which allow flexibility to merge two or more row or two or more column.
##  it require 2 parameter first the containt nrow and ncol then location of grid 
## where axes object is used to print  graph
a1=plt.subplot2grid((2,2),(0,1),rowspan=2) ## figrure is dived in 2X2 where our axis will target 1 tile.


a1.plot(x,x**2)
a1.set_title("Square")

a2=plt.subplot2grid((2,2),(0,0))
a2.plot(x,x**3)
a2.set_title("Cubic")

a3=plt.subplot2grid((2,2),(1,0))
a3.plot(x,np.exp(x))
a3.set_title("Expo")

plt.show()


fig,axes=plt.subplots(1,3,figsize=(12,8))

axes[0].plot(x,x**2)
axes[0].grid(True)
axes[0].set_title("Default grid")

axes[1].plot(x,x**2)
axes[1].grid(color="b",lw=0.25,ls="-.")

axes[1].set_title("Customer grid")

axes[2].plot(x,x**2)
axes[2].set_title("No grid")

plt.show()

