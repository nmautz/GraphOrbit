#ifndef ORBIT_SIMULATOR_H
#define ORBIT_SIMULATOR_H

#include <iostream>
#include <cmath>

bool num_in_range_of_x(double num, double x, double error);

std::pair<double, int> orbit(double x, double p, double error, int max, double (*func)(double));

double truncate_num(double num, int digits);

void run_orbit_sim(double x, double p, double error, int max_orbit, double (*func)(double));

#endif // ORBIT_SIMULATOR_H
