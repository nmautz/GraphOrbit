import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from orbit import f
import sys

# Define the cobweb function
def cobweb_iterate(x0, r, n_iter):
    x_values = [x0]
    y_values = [f(x0, r)]
    
    for _ in range(1, n_iter):
        x = y_values[-1]
        y = f(x, r)
        

        # check if x y has been seen before
        if x in x_values[:-2] and y in y_values[:-2]:
            # get list of all points between now and the duplicate
            duplicate_index = x_values.index(x)
            cycle_points = x_values[duplicate_index:] + y_values[duplicate_index:]
            print(f"Cycle detected at ({x},{y}) with {len(cycle_points)} points")
            break
        
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

# Define function to update plot
def update(frame):
    if frame == 0:
        return
    
    plt.clf()  # Clear the previous plot
    plt.grid(True)
    plt.plot(x_values[:frame], y_values[:frame], 'b-', linewidth=0.4)
    plt.plot([0, 1], [0, 1], 'k--', linewidth=1)  # Plot y=x line
    plt.title('Cobweb Diagram (c={})'.format(c))
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.plot(xs, ys, 'r-', linewidth=1)

#graph function on plot
xs = np.linspace(0, 1, 100)
ys = [f(x, c) for x in xs]

# Create animation
ani = FuncAnimation(plt.gcf(), update, frames=range(0, len(x_values), 1), interval=50, repeat=False)
plt.show()
