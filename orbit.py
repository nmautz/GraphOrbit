import numpy as np

def generate_c_values(left, right, num_steps):
    c_values = np.linspace(left+0.001, right-0.001, num_steps)
    return c_values.tolist()

def num_in_range_of_x(num, x, error):
    return abs(num - x) <= error

def orbit(x, max_iterations, func, func_prime,error):
    #output_file = open(filename, "w")
    plot_points = []
    last_x = None
    sum_lyapunov = 0
    iterations = 0
    for i in range(0,max_iterations):

        x = func(x)
        iterations +=1
        sum_lyapunov += np.log(np.abs(func_prime(x)))
        if last_x is not None:
            if num_in_range_of_x(x, last_x, error):
                return plot_points
        last_x = x
        #output_file.write(f"{x}\n")
        plot_points.append(x)


    lyapunov_exponent = sum_lyapunov/iterations
    return plot_points, lyapunov_exponent

def truncate_num(num, digits):
    return float(f"{num:.{digits}f}")
    

def run_orbit_sim(x, max_orbit, func, func_prime, c, cutoff,error):
    plot_points,lyapunov_exponent = orbit(x, max_orbit, func, func_prime,error)
    new_pp = []
    for point in plot_points:
        new_pp.append([c, point])

    new_pp = np.array(new_pp)
    # Only keep last 10%
    new_pp = new_pp[int(len(new_pp)*cutoff):]
    return new_pp, lyapunov_exponent
    
