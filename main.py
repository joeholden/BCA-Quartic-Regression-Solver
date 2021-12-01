import numpy as np
# Polynomial Regression
import matplotlib.pyplot as plt

x_s = [2000, 1500, 1000, 750, 500, 250, 125, 25, 0]
y_s = [1.84165, 1.41445, 1.04255, .86005, .5041, .39985, .28925, .1884, .1576]


def polyfit(x, y, degree):
    results = {}

    coefficients = np.polyfit(x, y, degree)
    results['polynomial'] = coefficients.tolist()

    p = np.poly1d(coefficients)

    y_hat = p(x)
    y_bar = np.sum(y) / len(y)
    ss_reg = np.sum((y_hat - y_bar) ** 2)
    ss_tot = np.sum((y - y_bar) ** 2)
    results['determination'] = ss_reg / ss_tot

    return results


def solve_quartic(solution_value):
    val = solution_value
    array = np.copy(polynomial_coefficients)
    array[-1] = array[-1] - val
    roots = np.roots(array)
    sorted_positive_roots = [np.real(i) for i in sorted(roots) if i > 0]
    first_positive_root = round(sorted_positive_roots[0], 2)

    return first_positive_root


def plot(x_scatter_standard, y_scatter_standard, polynomial, fit_x, fit_y):
    polynomial_cf = polynomial
    x = np.linspace(0, 2000, 1000)
    y = polynomial_cf[0] * x ** 4 + polynomial_cf[1] * x ** 3 + polynomial_cf[2] * x ** 2 \
        + polynomial_cf[3] * x + polynomial_cf[4]

    plt.scatter(x_s, y_s)
    plt.scatter(fit_x, fit_y, alpha=0.8)
    plt.plot(x, y)

    plt.show()


# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

regression_results = polyfit(x_s, y_s, 4)
global polynomial_coefficients
polynomial_coefficients = regression_results['polynomial']

r_squared = round(regression_results['determination'], 3)

print(f'R Squared: {r_squared}')

fit_points_y = [0.4441, 0.46075, 0.4334, 0.42435, 0.40865, 0.44505]
fit_points_x = []

for point in fit_points_y:
    c = solve_quartic(point)
    fit_points_x.append(c)

plot(x_s, y_s, polynomial_coefficients, fit_points_x, fit_points_y)





