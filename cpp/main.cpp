#include "orbit_simulator.h"

// Example of a function to be passed to run_orbit_sim
double example_function(double x) {
    // Replace this with your own function
    return std::sin(x);
}

int main() {
    // Example usage
    double x = 0.2;
    double p = 0.0;
    double error = 10e-8;
    int max_orbit = std::pow(10,100);

    run_orbit_sim(x, p, error, max_orbit, example_function);

    return 0;
}
