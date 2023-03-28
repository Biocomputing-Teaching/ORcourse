import numpy as np
import matplotlib.pyplot as plt

# Import the 'solve' and 'Symbol' functions from the sympy library
from sympy.solvers import solve
from sympy import Symbol

# Define the linear functions
def f1(x):
    return 7.-0.5*x
def f2(x):
    return 3.*x
def f3(x):
    return x-2.0

# Define x as a symbol
x = Symbol('x')

# Solve for the intersection points of the pairs of functions
x1, =  solve(f1(x)-f2(x))
x2, =  solve(f1(x)-f3(x))
x3, =  solve(f2(x)-f3(x))

# Calculate the y-coordinates of the intersection points
y1 = f1(x1)
y2 = f1(x2)
y3 = f2(x3)

# Find minimum and maximum values for x and y of the intersection points
x_min = float(min(x1, x2, x3))-1.
x_max = float(max(x1, x2, x3))+1.
y_min = float(min(y1, y2, y3))-1.
y_max = float(max(y1, y2, y3))+1.


# Plot each intersection point
plt.plot(x1,f1(x1),'go',markersize=10)
plt.plot(x2,f1(x2),'go',markersize=10)
plt.plot(x3,f2(x3),'go',markersize=10)

# Fill the area enclosed by the three functions
plt.fill([x1,x2,x3,x1],[y1,y2,y3,y1],'red',alpha=0.5)

# Create a range of x-values using linspace for each function
xr = np.linspace(int(x_min),int(x_max),100)
y1r = f1(xr)
y2r = f2(xr)
y3r = f3(xr)

# Plot each function with a dashed line type
plt.plot(xr,y1r,'k--')
plt.plot(xr,y2r,'k--')
plt.plot(xr,y3r,'k--')

# Set the x and y limits of the plot
plt.xlim(x_min,x_max)
plt.ylim(y_min,y_max)

# Show the plot
plt.show()