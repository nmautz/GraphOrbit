from orbit import run_orbit_sim, generate_c_values
import math
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter
import sys


gen_new = input("Generate new points? (y/n) ")
file_name = input("Enter file name: ")
if gen_new == "y":
  seed = 0

  left_interval = 4.72
  right_interval = 4.75
  num_steps_interval = 22500
  max_iter = 10000
  cutoff = 0.94
  error = 0.001
  c_values = generate_c_values(left_interval, right_interval, num_steps_interval)

  points = None
  i = 0
  for c in c_values:

    # Print % finished
    i += 1
    sys.stdout.write(f"{(i/len(c_values)) *100}% Complete                \r")
    sys.stdout.flush()
    
    f = lambda x: c * math.cos(x)
    n_points = run_orbit_sim(seed, max_iter, f, c, cutoff,error)
    if points is None:
      points = n_points
    else:
      points = np.concatenate((points, n_points))

  #Save points to file
  np.savetxt(file_name, points, fmt='%f')
elif gen_new == "n":
  #Load points from file
  points = np.loadtxt(file_name)
else:
  print("Invalid input")
  exit(0)






# Extract x and y coordinates
x = [point[0] for point in points]
y = [point[1] for point in points]


# Create a scatter plot with variable marker size
plt.scatter(x, y, marker='o', color='blue', label='Points', s=0.02, alpha=0.03)

# Add labels and title
plt.xlabel('c')
plt.ylabel('p')

# Show the legend
plt.legend()

# Show the plot
plt.grid(True)
plt.show()