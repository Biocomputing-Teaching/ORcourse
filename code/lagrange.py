import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

# Define the objective function f(x, y) = x^2 - y. You can also find the maximum of the math function by simply returnning the negative value of the python function
def objective(X):
    x, y = X
    return x**2 - y

# Define the constraint x^2 + y^2 = 4 (circle constraint)
def constraint(X):
    x, y = X
    return x**2 + y**2 - 4

# Initial guess (x0, y0). Try here different values to see the (bad) performance of the optimizer
x0 = [0, 2]

# Define the constraint as a dictionary
con = {'type': 'eq', 'fun': constraint}

# Solve the problem using 'minimize' with the SLSQP method (suitable for constrained optimization)
solution = minimize(objective, x0, method='SLSQP', constraints=[con])

# Get the optimal solution
x_opt, y_opt = solution.x

# Output the optimal solution
print(f"Optimal solution: x = {x_opt}, y = {y_opt}")
print(f"Minimum value of f(x, y) = {objective([x_opt, y_opt])}")

# Prepare to plot the system
x_vals = np.linspace(-2.5, 2.5, 400)
y_vals = np.linspace(-2.5, 2.5, 400)
X, Y = np.meshgrid(x_vals, y_vals)
F = X**2 - Y  # Objective function

# Define the constraint: circle x^2 + y^2 = 4
theta = np.linspace(0, 2*np.pi, 400)
x_circle = 2 * np.cos(theta)
y_circle = 2 * np.sin(theta)

# Plotting the objective function and constraint
plt.figure(figsize=(8, 6))
plt.contour(X, Y, F, levels=np.linspace(np.min(F), np.max(F), 50), cmap='coolwarm')
plt.plot(x_circle, y_circle, 'g-', label='$x^2 + y^2 = 4$ (Constraint)', linewidth=2)

# Mark the optimal point
plt.plot(x_opt, y_opt, 'ro', label=f'Optimal point (x={x_opt:.2f}, y={y_opt:.2f})')

# Labels and legend
plt.title('Contour Plot of $f(x, y) = x^2 - y$ with Constraint $x^2 + y^2 = 4$')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.colorbar(label='$f(x, y)$')

# Show the plot
plt.grid(True)
plt.show()
