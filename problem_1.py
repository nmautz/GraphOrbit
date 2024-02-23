from orbit import run_orbit_sim, generate_c_values
import math
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter



seed = 0

left_interval = -2.0
right_interval = 0.25
num_steps_interval = 100
max_iter = 10000
c_values = generate_c_values(left_interval, right_interval, num_steps_interval)

points = None
for c in c_values:

  f = lambda x: c + x**2
  n_points = run_orbit_sim(seed, max_iter, f, f"orbit_c_{c}.txt", c)
  if points is None:
    points = n_points
  else:
    points = np.concatenate((points, n_points))



# Extract x and y coordinates
x = [point[0] for point in points]
y = [point[1] for point in points]


# Create a scatter plot with variable marker size
plt.scatter(x, y, marker='o', color='blue', label='Points', s=0.001)

# Add labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Show the legend
plt.legend()

# Show the plot
plt.grid(True)
plt.show()