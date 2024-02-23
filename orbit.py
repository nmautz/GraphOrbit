import numpy as np

def generate_c_values(left, right, num_steps):
    c_values = np.linspace(left+0.001, right-0.001, num_steps)
    return c_values.tolist()

def num_in_range_of_x(num, x, error):
    return abs(num - x) <= error

def orbit(x, max_iterations, func, filename):
    output_file = open(filename, "w")
    for i in range(0,max_iterations):
        new_x = func(x)
        if new_x == x:
            return x, i
        x = new_x
        output_file.write(f"{x}\n")
    print()
    return x, max_iterations

def truncate_num(num, digits):
    return float(f"{num:.{digits}f}")
    

def run_orbit_sim(x, max_orbit, func, orbit_filename):
    round_to = 10
    orbit_number, iterations = orbit(x, max_orbit, func, orbit_filename)

    print(f"The orbit number is {truncate_num(orbit_number, round_to)} and the number of iterations is {iterations}")


