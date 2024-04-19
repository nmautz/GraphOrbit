import multiprocessing.process
import numpy as np
import copy
import multiprocessing
from functools import partial

def generate_c_values(left, right, num_steps):
    c_values = np.linspace(left+0.001, right-0.001, num_steps)
    return c_values.tolist()

def num_in_range_of_x(num, x, error):
    return abs(num - x) <= error

def numerical_derivative(f, x, h=1e-5):
    value = None
    try:
        # Try the center difference formula
        value = (f(x + h) - f(x - h)) / (2 * h)
    except Exception as e:
        try:
            # Try right difference formula
            value =  (f(x + h) - f(x)) / h
        except Exception as e:
            # Try left difference formula
            value=  (f(x) - f(x - h)) / h

    finally:
        return value

def orbit(x, max_iterations, func,error):
    #output_file = open(filename, "w")
    plot_points = []
    last_x = None
    sum_lyapunov = 0
    iterations = 0
    for i in range(0,max_iterations):
        x = func(x)
        deriv_val = numerical_derivative(func, x)
        if deriv_val is not None:
            iterations +=1
            sum_lyapunov += np.log(np.abs(deriv_val))
        else:
            print("ERROR: derivitive is None")
        if last_x is not None and error != 0:
            if num_in_range_of_x(x, last_x, error):
                lyapunov_exponent = sum_lyapunov/iterations
                return plot_points, lyapunov_exponent

        last_x = x
        #output_file.write(f"{x}\n")
        plot_points.append(x)
    try:
        lyapunov_exponent = sum_lyapunov/iterations
    except:
        print("ERROR: sum_lyapunov/iterations")
        lyapunov_exponent = 400

    
    return plot_points, lyapunov_exponent

def truncate_num(num, digits):
    return float(f"{num:.{digits}f}")
    

function_error = 0.0001
def round_to_function_error(num):
    rounded_num = round(num / function_error) * function_error
    return rounded_num


def f(x,c):

    if not c > 1:
        raise Exception("c must be greater than 1")

    if 0 <= x <= 1/c:
        return round_to_function_error(c*x)
    elif 1/c <= x <= 1:
        return round_to_function_error(c*(x-1)/(1-c))
    else:
        raise Exception("x must be between 0 and 1")

def simulate_orbit(c, x=0.1, max_orbit = 10000, error=0.001, cutoff=0.94):
    func = partial(f, c=c)
    plot_points, lyapunov_exponent = orbit(x, max_orbit, func, error)
    new_pp = []
    for point in plot_points:
        new_pp.append([c, point])
    new_pp = np.array(new_pp)
    new_pp = new_pp[int(len(new_pp)*cutoff):]  # Only keep last cutoff portion
    
    return tuple([new_pp, lyapunov_exponent, c])