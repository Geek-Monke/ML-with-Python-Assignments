
import numpy as np
import pandas as pd
my_arr = np.ones((4, 6))
print("4x6 Array filled with ones:\n", my_arr)

non_zero_count = np.count_nonzero(my_arr)
print("Number of non-zero values:", non_zero_count)

element_count = my_arr.shape[0]
print("Number of elements along the rows axis:", element_count)

one_d_arr = np.array([0, 0, 1, 2, 3, 0, 0])
trimmed_arr = np.trim_zeros(one_d_arr)
print("Trimmed 1-D array:", trimmed_arr)

reversed_arr = my_arr[::-1, ::-1]
print("Reversed array:\n", reversed_arr)

diagonal_sum = np.trace(my_arr)
print("Sum of diagonal elements:", diagonal_sum)

matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])
added_matrix = matrix1 + matrix2
subtracted_matrix = matrix1 - matrix2
print("Added matrix:\n", added_matrix)
print("Subtracted matrix:\n", subtracted_matrix)

new_row = np.array([[1, 1, 1, 1, 1, 1]])
my_arr = np.vstack([my_arr, new_row])
print("Array after adding a row:\n", my_arr)

new_col = np.array([[1], [1], [1], [1], [1]])
my_arr = np.hstack([my_arr, new_col])
print("Array after adding a column:\n", my_arr)

matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])
multiplied_matrix = np.dot(matrix1, matrix2)
print("Matrix multiplication result:\n", multiplied_matrix)