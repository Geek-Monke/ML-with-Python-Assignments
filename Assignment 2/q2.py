import pandas as pd
import numpy as np

my_arr = np.ones((3, 4))
print("Array filled with ones:\n", my_arr)

my_arr += 5
print("Array after adding 5:\n", my_arr)

my_arr_log = np.log(my_arr)
print("Element-wise logarithm of the array:\n", my_arr_log)

arr_mean = np.mean(my_arr)
print("Mean of the array:", arr_mean)

arr_std = np.std(my_arr)
print("Standard deviation of the array:", arr_std)

arr_sum = np.sum(my_arr)
print("Sum of the array:", arr_sum)

arr_max = np.max(my_arr)
print("Max value in the array:", arr_max)

arr_max_idx = np.argmax(my_arr)
print("Index of the max value in the array:", arr_max_idx)

arr_mean_rows = np.mean(my_arr, axis=1)
print("Mean along the rows axis:", arr_mean_rows)