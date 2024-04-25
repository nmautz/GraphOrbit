import matplotlib.pyplot as plt
import numpy as np
import sys
from orbit import simulate_orbit

# Get argv
try:
    seed = float(sys.argv[1])
    c = float(sys.argv[2])
except:
    print("Usage: python3 seed c")
    exit()

points, _, _ = simulate_orbit(c, seed, cutoff=0, max_orbit=10000000)

point_y_values = [p[1] for p in points]

# normalize y values 
point_y_values = [y/max(point_y_values) for y in point_y_values]

# plot histogram of y values
plt.hist(point_y_values, bins=100)
plt.show()
