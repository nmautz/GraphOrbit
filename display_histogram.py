import matplotlib.pyplot as plt
import numpy as np
import sys

# Get argv
try:
    file_name = sys.argv[1]
    points = np.loadtxt(file_name)
except Exception as e:
    print(e)
    print(f"Usage: python3 {sys.argv[0]} <file_name>")
    exit()

# Extract x and y coordinates
x = [point[0] for point in points]
y = [point[1] for point in points]

# Find range of x 
x_min = min(x)
x_max = max(x)

# Calculate histogram
hist, bins = np.histogram(x, bins=10)  # Adjust the number of bins as needed

# Normalize the histogram
hist = hist / np.sum(hist)

# Plot histogram
plt.bar(bins[:-1], hist, width=np.diff(bins), align='edge')
plt.xlabel('X')
plt.ylabel('Frequency')
plt.title(f'Normalized Histogram of X Values, {x_min} <= x <= {x_max}')
plt.show()
