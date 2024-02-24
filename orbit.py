import numpy as np

def generate_c_values(left, right, num_steps):
    c_values = np.linspace(left+0.001, right-0.001, num_steps)
    return c_values.tolist()

def num_in_range_of_x(num, x, error):
    return abs(num - x) <= error

def orbit(x, max_iterations, func, filename):
    #output_file = open(filename, "w")
    plot_points = []
    for i in range(0,max_iterations):
        x = func(x)
        #output_file.write(f"{x}\n")
        plot_points.append(x)

    return plot_points

def truncate_num(num, digits):
    return float(f"{num:.{digits}f}")
    

def run_orbit_sim(x, max_orbit, func, orbit_filename, c):
    plot_points = orbit(x, max_orbit, func, orbit_filename)
    new_pp = []
    for point in plot_points:
        new_pp.append([c, point])

    new_pp = np.array(new_pp)
    # Only keep last 10%
    new_pp = new_pp[int(len(new_pp)*0.99998):]
    return new_pp
    
