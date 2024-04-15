from orbit import run_orbit_sim, generate_c_values
import math
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter
import sys


# Get argv
try:
  file_name = sys.argv[1]
  points = np.loadtxt(file_name)
  lyapunov_exponents = np.load("l_ex_"+file_name+".npy", allow_pickle=True).item()
except Exception as e:
  print(e)
  print(f"Usage: python3 {sys.argv[0]} <file_name>")
  exit()


# Extract x and y coordinates
x = [point[0] for point in points]
y = [point[1] for point in points]

# split lyapunov dict into x and y
lx = np.array(list(lyapunov_exponents.keys())) 
ly = np.array(list(lyapunov_exponents.values()))


# Create a scatter plot with variable marker size
plt.scatter(x, y, marker='o', color='blue', label='Points', s=0.02, alpha=0.03)
plt.scatter(lx, ly, marker='o', color='red', label='Lyapunov Exponents', s=0.2, alpha=0.2)
# Add labels and title
plt.xlabel('c')
plt.ylabel('p')

# Show the legend
plt.legend()

# Show the plot
plt.grid(True)
plt.show()