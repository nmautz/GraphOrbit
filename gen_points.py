from orbit import run_orbit_sim, generate_c_values
import math
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter
import sys
import time




file_name = input("Enter file name: ")
initial_time = time.time()

seed = 0

left_interval = -1.5
right_interval = -1.25
num_steps_interval = 200
max_iter = 1000
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
  
  f = lambda x: x**2 +c
  n_points = run_orbit_sim(seed, max_iter, f, c, cutoff,error)
  if points is None:
    points = n_points
  else:
    points = np.concatenate((points, n_points))

#Save points to file
np.savetxt(file_name, points, fmt='%f')

final_time = time.time()
elapsed_seconds = final_time - initial_time
print(f"Finished in {elapsed_seconds} seconds.")