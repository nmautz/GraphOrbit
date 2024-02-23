#include "orbit_simulator.h"

bool num_in_range_of_x(double num, double x, double error) {
    return std::abs(num - x) <= error;
}

std::pair<double, int> orbit(double x, double p, double error, int max, double (*func)(double)) {
    for (int i = 0; i < max; ++i) {
        if (i % max/ == 0) {
            std::cout << i << ": " << x << std::endl;
        }
        x = func(x);
        if (num_in_range_of_x(x, p, error)) {
            std::cout << std::endl;
            return std::make_pair(x, i);
        }
    }
    std::cout << std::endl;
    return std::make_pair(-1, max);
}

double truncate_num(double num, int digits) {
    return std::stod(std::to_string(num).substr(0, std::to_string(num).find('.') + digits + 1));
}

void run_orbit_sim(double x, double p, double error, int max_orbit, double (*func)(double)) {
    int round_to = 10;
    auto result = orbit(x, p, error, max_orbit, func);
    std::cout << "The orbit number is " << truncate_num(result.first, round_to)
              << " and the number of iterations is " << result.second << std::endl;
}
