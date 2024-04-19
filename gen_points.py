from orbit import generate_c_values, simulate_orbit
import math
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter
import sys
import time
import multiprocessing
import subprocess
import cProfile
def main():
  # Get argv
  try:
    file_name = sys.argv[1]
  except Exception as e:
    print(e)
    print(f"Usage: python3 {sys.argv[0]} <file_name>")
    exit()

  try:
    display_after = int(sys.argv[2])
  except Exception as e:
    display_after = -1
    
  initial_time = time.time()
  left_interval = 1.1
  right_interval = 10
  num_steps_interval = 5000

  c_values = generate_c_values(left_interval, right_interval, num_steps_interval)

  points = None
  lyapunov_exponents = {}
  i = 0



  pool = multiprocessing.Pool(processes=multiprocessing.cpu_count() - 1)
  arg_list_list = []
  print("Generating arguments")
  for c_val in c_values:
    arg_list_list.append([c_val])
    i+=1
    if i % 1000 == 0:
      print(f"Generated {i}/{len(c_values)} arguments")
  print("Starting processes")
  print("Waiting for processes to finish...")

  #pool.starmap(simulate_orbit, arg_list_list)
  results = (pool.starmap(simulate_orbit, arg_list_list))

  pool.close()
  pool.join()

  i=0
  print("Parsing results")
  number_point_arrays = len(results)
  points_list = np.empty(number_point_arrays, dtype=object)
  for n_points, lyapunov_exponent, c in results:
    #parse results n_points, lenoponov, c
    lyapunov_exponents[c] = lyapunov_exponent
    points_list[i] = n_points

    i=i+1
    if i % 1000 == 0:
      print(f"Parsed {i}/{len(results)} results")

  points = np.concatenate(points_list)
  print("Saving to disk...")

  #Save points to file
  np.savetxt(file_name, points, fmt='%f')
  #Save lyapunov exponents to file
  np.save("l_ex_"+file_name, lyapunov_exponents)  

  final_time = time.time()
  elapsed_seconds = final_time - initial_time
  print(f"Finished in {elapsed_seconds} seconds.")


  if display_after >= 0:
    # run cli input
    print("Displaying points...")
    subprocess.run(["python3", 'display_points.py', file_name, str(display_after)])

if __name__ == "__main__":
  main()