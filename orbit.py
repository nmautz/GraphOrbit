
def num_in_range_of_x(num, x, error):
    return abs(num - x) <= error

def orbit(x, p, error, max, func):
    for i in range(0,max):
        if i % (max/(10**4)) == 0:
            print(f"{i}: {x}", end='\r', flush=True)
        x = func(x)
        if num_in_range_of_x(x, p, error):
            print()
            return x,i
    print()
    return -1, max

def truncate_num(num, digits):
    return float(f"{num:.{digits}f}")
    

def run_orbit_sim(x, p, error, max_orbit, func):
    round_to = 10
    orbit_number, iterations = orbit(x, p, error, max_orbit, func)
    print(f"The orbit number is {truncate_num(orbit_number, round_to)} and the number of iterations is {iterations}")


