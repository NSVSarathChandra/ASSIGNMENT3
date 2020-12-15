import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA

#Equation for circle
#X^T - 2c^T + f = 0 

#Input parameters
P = np.array(([2,3]))
Q = np.array(([3,2]))
R = np.array(([5,1]))

X = np.array((2*P, 2*Q, 2*R))
Y = np.array(([-1],[-1],[-1]))
A = np.append(X, Y, axis=1)
B = np.array(([13,13,26]))

#Calculating the Center and radius
X2 = LA.solve(A,B)

C = np.array((X2[0],X2[1]))
f = X2[2]

r = np.sqrt(LA.norm(C)**2-f)

print("Radius of the circle:")
print("{:>.3f}".format(r))
print("Central coordinate (x, y) of the circle:")
print(C)

#Plotting the circle
plt.figure()
fig, ax = plt.subplots()
ax.add_patch(plt.Circle(C, r, color='r', fill=False))


#Labeling the coordinates
tri_coords = np.vstack((P,Q,R,C)).T
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['P','Q','R','C']
for i, txt in enumerate(vert_labels):
    plt.annotate(txt, # this is the text
                 (tri_coords[0,i], tri_coords[1,i]), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.grid() # minor
plt.axis('equal')

plt.show()