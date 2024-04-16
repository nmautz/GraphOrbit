from orbit import generate_c_values, OrbitSimThread
import math
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter
import sys
import time




# Get argv
try:
  file_name = sys.argv[1]
except Exception as e:
  print(e)
  print(f"Usage: python3 {sys.argv[0]} <file_name>")
  exit()
  
initial_time = time.time()

seed = 0.1

left_interval = 1
right_interval = 5
num_steps_interval = 20000
max_iter = 10000
cutoff = 0.94
error = 0.001
c_values = generate_c_values(left_interval, right_interval, num_steps_interval)

points = None
lyapunov_exponents = {}
i = 0
threads = []
for c in c_values:
  f = lambda x: c*x if 0 <= x <= 1/c else c*(x-1)/(1-c) if 1/c <= x <= 1 and c > 1 else None
  orbit_thread = OrbitSimThread(seed, max_iter, f, c, cutoff,error)
  threads.append(orbit_thread)
  

print(f"Starting {len(threads)} threads...")
for thread in threads:
  thread.start()

print("Waiting for threads to finish...")

for thread in threads:
  thread.join()
  #parse results n_points, lenoponov, c
  results_tuple = thread.results()
  n_points = results_tuple[0]
  print(len(n_points))
  lyapunov_exponent = results_tuple[1]
  print(lyapunov_exponent)

  c = results_tuple[2]
  print(f"Thread c={c} finished.")

  lyapunov_exponents[c] = lyapunov_exponent
  if points is None:
    points = n_points
  else:
    points = np.concatenate((points, n_points))

print("Finished simulating all c values.")

#Save points to file
np.savetxt(file_name, points, fmt='%f')
#Save lyapunov exponents to file
np.save("l_ex_"+file_name, lyapunov_exponents)  

final_time = time.time()
elapsed_seconds = final_time - initial_time
print(f"Finished in {elapsed_seconds} seconds.")