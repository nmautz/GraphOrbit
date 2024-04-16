from orbit import generate_c_values, OrbitSimProcess
import math
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter
import sys
import time
import multiprocessing


if __name__ == "__main__":
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
  right_interval = 500
  num_steps_interval = 2000
  max_iter = 10000
  cutoff = 0.94
  error = 0.001
  c_values = generate_c_values(left_interval, right_interval, num_steps_interval)

  points = None
  lyapunov_exponents = {}
  i = 0
  orbit_result_tuple_arr = []



  result_manager = multiprocessing.Manager()
  print(f"Creating {len(c_values)} processes...")
  for c_val in c_values:
    result_queue = result_manager.Queue()
    orbit_process = OrbitSimProcess(seed, max_iter, c_val, cutoff,error, result_queue)
    orbit_result_tuple_arr.append((orbit_process, result_queue))
    
  num_processes = len(orbit_result_tuple_arr)
  print(f"Starting {num_processes} processes...")
  for orbit_process,_ in orbit_result_tuple_arr:
    orbit_process.start()
    i=i+1
    if i%500 == 0:
      print(f"Thread {i}/{num_processes} started.")

  print("Waiting for processes to finish...")

  i=0
  for orbit_process, result_queue in orbit_result_tuple_arr:
    orbit_process.join()
    i=i+1
    #parse results n_points, lenoponov, c
    results_tuple = result_queue.get()
    n_points = results_tuple[0]
    lyapunov_exponent = results_tuple[1]

    c = results_tuple[2]
    if i%500 == 0:
      print(f"Thread {i}/{num_processes} finished.")

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