# Import numpy
import numpy as np

# Function to get adjoint
def get_adjoint(matrix):
    # Calculate the adjoint of the matrix
    adjoint = np.linalg.inv(matrix).T * np.linalg.det(matrix)
    return adjoint

# Function to get determinant
def get_determinant(matrix):
    # Calculate the determinant of the matrix
    determinant = np.linalg.det(matrix)
    return determinant

# Function to get transpose
def get_transpose(matrix):
    # Calculate the transpose of the matrix
    transpose = np.transpose(matrix)
    return transpose

# Example for usage:
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

# Function objects
adjoint = get_adjoint(matrix)
determinant = get_determinant(matrix)
transpose = get_transpose(matrix)

# Showing answers
print("Matrix:")
print(matrix)

print("Adjoint:")
print(adjoint)

print("Determinant:")
print(determinant)

print("Transpose:")
print(transpose)
