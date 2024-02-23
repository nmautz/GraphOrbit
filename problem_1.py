from orbit import run_orbit_sim, generate_c_values
import math


seed = 0

left_interval = -0.75
right_interval = 0.25
num_steps_interval = 5
max_iter = 10000
c_values = generate_c_values(left_interval, right_interval, num_steps_interval)
for c in c_values:

  f = lambda x: c + x**2
  run_orbit_sim(seed, max_iter, f, f"orbit_c_{c}.txt")