import numpy as np

def generate_c_values(left, right, num_steps):
    c_values = np.linspace(left, right, num_steps)
    return c_values.tolist()

def num_in_range_of_x(num, x, error):
    return abs(num - x) <= error

def orbit(x, p, error, max_iterations, func):
    for i in range(0,max_iterations):
        if i % (max_iterations/(10**4)) == 0:
            print(f"{i}: {x}", end='\r', flush=True)
        x = func(x)
        if num_in_range_of_x(x, p, error):
            print()
            return x,i
    print()
    return -1, max_iterations

def truncate_num(num, digits):
    return float(f"{num:.{digits}f}")
    

def run_orbit_sim(x, p, error, max_orbit, func):
    round_to = 10
    if num_in_range_of_x(x,p,error):
        orbit_number = 0
        iterations = 0
    else:
        orbit_number, iterations = orbit(x, p, error, max_orbit, func)

    print(f"The orbit number is {truncate_num(orbit_number, round_to)} and the number of iterations is {iterations}")


