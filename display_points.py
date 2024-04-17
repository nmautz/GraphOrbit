import matplotlib.pyplot as plt
import numpy as np
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


density_multiplier = 2
# get range of x values
x_min = min(x)
x_max = max(x)
# get count of y values
y_count = len(y)

desired_point_size = ((x_max - x_min) / y_count) * 30000 * density_multiplier
print(desired_point_size)



# Create a scatter plot with variable marker size
plt.scatter(x, y, marker='o', color='blue', label='Points', s=desired_point_size, alpha=0.03)
plt.scatter(lx, ly, marker='o', color='red', label='Lyapunov Exponents', s=0.2, alpha=0.2)
# Add labels and title
plt.xlabel('c')
plt.ylabel('p')

# Show the legend
plt.legend()

# Show the plot
plt.grid(True)
plt.show()