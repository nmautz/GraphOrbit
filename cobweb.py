import numpy as np
import matplotlib.pyplot as plt
from orbit import f
import sys

# Define the cobweb function
def cobweb_iterate(x0, r, n_iter):
    x_values = [x0]
    y_values = [f(x0, r)]
    
    for _ in range(1, n_iter):
        x = y_values[-1]
        y = f(x, r)
        
        x_values.extend([x, y])
        y_values.extend([y, y])
    
    return x_values, y_values

# Parameters
x0 = 0.1  # Initial value
c = 1.1  # Parameter value
n_iter = 50  # Number of iterations

try:
    x0 = float(sys.argv[1])
    c = float(sys.argv[2])
    n_iter = int(sys.argv[3])
except Exception as e:
    print("Error with params, using defaults")
    print(f"x0={x0}")
    print(f"c={c}")
    print(f"n_iter={n_iter}")

# Generate cobweb data
x_values, y_values = cobweb_iterate(x0, c, n_iter)

# Plot cobweb diagram
plt.plot(x_values, y_values, 'b-', linewidth=0.5)
plt.plot([0, 1], [0, 1], 'k--', linewidth=1)  # Plot y=x line
plt.title('Cobweb Diagram(c={})'.format(c))
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.show()
