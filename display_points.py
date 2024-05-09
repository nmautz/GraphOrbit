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

try:
  optimized = int(sys.argv[2])
except:
  optimized = 0


# Extract x and y coordinates
x = [point[0] for point in points]
y = [point[1] for point in points]

py = []
for i in range(0, len(x)):
  a = x[i]
  py.append(a/((a*a)+a-1))

# split lyapunov dict into x and y
lx = np.array(list(lyapunov_exponents.keys())) 
ly = np.array(list(lyapunov_exponents.values()))


density_multiplier = 40000
# get range of x values
x_min = min(x)
x_max = max(x)
# get count of y values
y_count = len(y)

desired_point_size = (1/y_count) * density_multiplier
desired_point_size = min(desired_point_size, 15)

# Hide the plot
plt.grid(False)

# Create a scatter plot with variable marker size
if optimized:
  plt.hexbin(x, y, gridsize=optimized, cmap='plasma', alpha=1, mincnt=1)  # Adjust gridsize as needed
  #plt.scatter(lx, ly, marker='o', color='green', label='Lyapunov Exponents', s=0.5, alpha=1)
else:
  plt.scatter(x, y, marker='o', color='blue', label='Points', s=desired_point_size, alpha=0.03)
  plt.scatter(x, py, marker='o', color='red', label='Repelling Orbit point', s=0.2, alpha=0.2)
# Add labels and title
plt.xlabel('c')
plt.ylabel('p')

# Show the legend
#plt.legend()


plt.show()