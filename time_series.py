
from orbit import simulate_orbit
import sys
import numpy as np
import matplotlib.pyplot as plt
  
seed_1 = 0.3000001
seed_2 = 0.3000002
c = 400

max_orbit = 200
drop_first_values = 100

points_1, _,_ = simulate_orbit(c, seed_1, max_orbit=max_orbit, error=0, cutoff=0)

points_2, _,_ = simulate_orbit(c, seed_2, max_orbit=max_orbit, error=0, cutoff=0)
point_1_parsed = []
point_2_parsed = []
#throw out c values and replace with step num
for i in range(drop_first_values, len(points_1)):
    point = points_1[i]
    point_1_parsed.append([i, point[1]])

for i in range(drop_first_values, len(points_2)):
    point = points_2[i]
    point_2_parsed.append([i, point[1]])

point_1_x, point_1_y = zip(*point_1_parsed)
point_2_x, point_2_y = zip(*point_2_parsed)

# Calculate variance


print(f"Plotting {len(point_1_parsed) + len(point_2_parsed)} points")

plt.plot(point_1_x, point_1_y, label=f"Seed: {seed_1}", color="red", alpha=0.5)
plt.plot(point_2_x, point_2_y, label=f"Seed: {seed_2}", color="blue", alpha=0.5)
plt.title(f"C: {c}")
plt.xlabel('Step')
plt.ylabel('p')
plt.legend()
plt.show()