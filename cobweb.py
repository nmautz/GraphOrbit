import numpy as np
import matplotlib.pyplot as plt
from orbit import f

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
