import matplotlib.pyplot as plt
import numpy as np
import sys
from orbit import simulate_orbit

# Get argv
try:
    seed = float(sys.argv[1])
    c = float(sys.argv[2])
    max_orbit = int(sys.argv[3])
except:
    print("Usage: python3 seed c max_orbit")
    exit()

points, _, _ = simulate_orbit(c, seed, cutoff=0.94, max_orbit=10000)

point_y_values = [p[1] for p in points]


# plot histogram of y values
plt.hist(point_y_values, bins=100)
plt.title(f"Seed: {seed}\nc:{c}\niterations:{max_orbit}")
plt.show()
