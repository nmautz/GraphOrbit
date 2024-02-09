from orbit import run_orbit_sim
import math

def f(x):
  return x**2 + 0.25

run_orbit_sim(0.2, 0.5, 10**-8, 10**10, f)
