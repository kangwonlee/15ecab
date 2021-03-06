import math
import root_finding


def main():
    root_finding.epsilon = 1e-9
    r_init = root_finding.epsilon
    delta_r = 1e-6
    result = root_finding.sequential(problem_to_solve, r_init, delta_r)
    print "result =", result
    print "f(result)=", problem_to_solve(result)

    result_bisection = root_finding.bisection(problem_to_solve, result - delta_r, result)
    print "result_bisection =", result_bisection
    print "f(result_bisection) =", problem_to_solve(result_bisection)

    help(root_finding.sequential)


def problem_to_solve(radius_m):
    force_N = 100.0
    stress_max_Pa = 207e6
    safety_factor = 2.0
    return circular_section_stress(radius_m, force_N) - stress_max_Pa / safety_factor


def df_dr(radius_m):
    force_N = 100.0
    result = (force_N * (-2.0) / math.pi) / (radius_m**3)
    return result


def circular_section_stress(r_m, force_N):
    area_m2 = r_m * r_m * math.pi
    stress_Pa = force_N / area_m2
    return stress_Pa


if "__main__" == __name__:
    main()
