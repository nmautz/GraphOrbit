import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from orbit import f, truncate_num
import sys

# Define the cobweb function
def cobweb_iterate(x0, r, n_iter):
    x_values = [x0]
    y_values = [f(x0, r)]
    cycle_points_xs = []
    cycle_points_ys = []
    
    for i in range(1, n_iter):
        x = y_values[-1]
        y = f(x, r)

        if i % 5000 == 0:
            print(f"Iteration #{i}/{n_iter} ({truncate_num(100*(i/n_iter),1)}%)")
        

        # check if x y has been seen before
        if x in x_values[:-2] and y in y_values[:-2]:
            duplicate_index = x_values.index(x)
            cycle_points_xs = x_values[duplicate_index:]
            print(f"Cycle detected at iteration #{i} with {len(cycle_points_xs)/3} points")
            print(f"Starting Point: {({x},{y}) }")
            x_values.extend([x, y])
            y_values.extend([y, y])
            x = y_values[-1]
            y = f(x, r)
            x_values.extend([x, y])
            y_values.extend([y, y])
            # get list of all points between now and the duplicate
            cycle_points_xs = x_values[duplicate_index:]
            cycle_points_ys = y_values[duplicate_index:]
            break
        x_values.extend([x, y])
        y_values.extend([y, y])
    return x_values, y_values, cycle_points_xs, cycle_points_ys

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
x_values, y_values, cycle_points_xs, cycle_points_ys = cobweb_iterate(x0, c, n_iter)

# Define function to update plot
def update(frame):
    if frame == 0:
        return
    plt.clf()  # Clear the previous plot
    plt.grid(True)
    plt.plot(x_values[:frame], y_values[:frame], 'b-', linewidth=0.8)
    plt.plot([0, 1], [0, 1], 'k--', linewidth=1)  # Plot y=x line
    current_value = current_value = f(x_values[frame], c)
    plt.title(f"Seed: {x0} C:{c}\nStep:{frame}/{len(x_values)}\nx:{current_value}")
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.plot(xs, ys, 'r-', linewidth=1)

#graph function on plot
xs = np.linspace(0, 1, 100)
ys = [f(x, c) for x in xs]

if(cycle_points_xs != []):
    plt.figure(2)
    plt.title('Cycle Points (c={})'.format(c))
    plt.plot(cycle_points_xs, cycle_points_ys, 'b-', linewidth=0.4)
    plt.plot([0, 1], [0, 1], 'k--', linewidth=0.4)  # Plot y=x line
    plt.plot(xs, ys, 'r-', linewidth=1)
    plt.show()
else:
    print(f"No cycle detected in first {n_iter}")

try:
    show_anim = sys.argv[4]
except Exception as e:
    print("Showing no anim (default)")
    show_anim = 0


if show_anim:
    # Create animation
    ani = FuncAnimation(plt.gcf(), update, frames=range(0, len(x_values), 1), interval=5, repeat=True)
else:
    # graph all normally
    plt.grid(True)
    plt.plot(x_values, y_values, 'b-', linewidth=0.4)
    plt.plot([0, 1], [0, 1], 'k--', linewidth=1)  # Plot y=x line
    plt.title(f"Seed: {x0} C:{c}\n")
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.plot(xs, ys, 'r-', linewidth=1)

plt.show()



