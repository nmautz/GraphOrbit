from orbit import run_orbit_sim, generate_c_values
import math


def find_fixed_points(c):
  inner = 1-(4*c)
  if inner < 0:
    return [0, 0]
  sqrt_p = math.sqrt(inner)
  p = (1+sqrt_p)/2
  q = (1-sqrt_p)/2
  return [p, q]

seed = 0

left_interval = -0.75
right_interval = 0.25
num_steps_interval = 5
max_iter = 1000000
c_values = generate_c_values(left_interval, right_interval, num_steps_interval)
for c in c_values:

  f = lambda x: c + x**2
  fps = find_fixed_points(c)
  print(f"c = {c}")
  print(f"Fixed points: {fps}")
  run_orbit_sim(seed, fps[0], 0.0001, max_iter, f)
  run_orbit_sim(seed, fps[1], 0.0001, max_iter, f)