from orbit import run_orbit_sim, generate_c_values
import math
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter
import sys


file_name = input("Enter file name: ")
points = np.loadtxt(file_name)

# Extract x and y coordinates
x = [point[0] for point in points]
y = [point[1] for point in points]


# Create a scatter plot with variable marker size
plt.scatter(x, y, marker='o', color='blue', label='Points', s=0.02, alpha=0.03)

# Add labels and title
plt.xlabel('c')
plt.ylabel('p')

# Show the legend
plt.legend()

# Show the plot
plt.grid(True)
plt.show()