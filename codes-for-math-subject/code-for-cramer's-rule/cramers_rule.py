# Import numpy module
import numpy as np

# Function to solve cramer's problem
def cramer_solver(coefficients, constants):
    """
    Solves a system of linear equations using Cramer's rule.
    :param coefficients: 2D array representing the coefficients of the variables.
    :param constants: 1D array representing the constants.
    :return: 1D array of solutions for each variable.
    """
    det_a = np.linalg.det(coefficients)

    if det_a == 0:
        raise ValueError("The system of equations does not have a unique solution.")

    num_variables = len(coefficients[0])
    solutions = []

    for i in range(num_variables):
        submatrix = np.copy(coefficients)
        submatrix[:, i] = constants
        det_submatrix = np.linalg.det(submatrix)
        solutions.append(det_submatrix / det_a)

    return solutions

# Example for usage:
temp_coefficients = np.array([[2, 1, -1],
                         [3, 4, 2],
                         [1, -3, 5]])

temp_constants = np.array([4, 10, 12])

temp_solutions = cramer_solver(temp_coefficients, temp_constants)

print("Solution:", temp_solutions)
