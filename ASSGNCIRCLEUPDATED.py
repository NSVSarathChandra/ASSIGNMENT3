import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA

import sys                                          #for path to external scripts
sys.path.insert(0, '/storage/emulated/0/tlc/school/ncert/linman/codes/CoordGeo')        #path to my scripts

#local imports
from line.funcs import *
from triangle.funcs import *
from conics.funcs import circ_gen

#if using termux
import subprocess
import shlex
#end if

#Input parameters
[x1, y1] = [2,3]
[x2, y2] = [3,2]
[x3, y3] = [5,1]

#Calculation of central coordinates of the circle

c = (x1-x2)**2 + (y1-y2)**2
a = (x2-x3)**2 + (y2-y3)**2
b = (x3-x1)**2 + (y3-y1)**2

s = 2*(a*b + b*c + c*a) - (a*a + b*b + c*c)

#Central Coordinates of the circle
cx = (a*(b+c-a)*x1 + b*(c+a-b)*x2 + c*(a+b-c)*x3) / s
cy = (a*(b+c-a)*y1 + b*(c+a-b)*y2 + c*(a+b-c)*y3) / s 

#Calculation of radius of the circle 
ar = a**0.5
br = b**0.5
cr = c**0.5

#Radius of the Cirle
r = ar*br*cr / ((ar+br+cr)*(-ar+br+cr)*(ar-br+cr)*(ar+br-cr))**0.5

print("Radius of the circle:")
print("{:>.3f}".format(r))
print("Central coordinate (x, y) of the circle:")
print("{:>.3f}".format(cx),"{:>.3f}".format(cy))

#Plotting the circle and marking the points

X = np.array([[x1, y1], [x2, y2], [x3, y3], [cx, cy]])
Y = ['blue', 'blue', 'blue', 'blue']

plt.figure()

fig, ax = plt.subplots()
ax.add_patch(plt.Circle((cx, cy), r, color='r', fill=False))
plt.scatter(X[:, 0], X[:, 1], s = 20, color = Y[:])

plt.xlabel('X')
plt.ylabel('Y')

#Labeling the coordinates
for x,y in X:

    label = f"({x},{y})"

    plt.annotate(label, # this is the text
                 (x,y), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

ax.set_aspect('equal')
ax.plot()
#if using termux
plt.savefig('./figs/circex/CircOr.pdf')
plt.savefig('./figs/circex/CircOr.png')
subprocess.run(shlex.split("termux-open ./figs/circex/CircOr.pdf"))
#else
#plt.show()
