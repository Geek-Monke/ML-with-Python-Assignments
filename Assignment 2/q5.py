import numpy as np

# Create a Numpy array filled with ones with 4 rows and 6 columns
my_arr = np.ones((4, 6))

# a) Indices of the sorted array
sorted_indices = np.argsort(my_arr, axis=None)

# b) Find the k smallest values of a Numpy array
k = 3
flattened_array = my_arr.flatten()
k_smallest_values = np.partition(flattened_array, k)[:k]

# c) Get the n-largest values of an array
n = 3
n_largest_values = np.partition(flattened_array, -n)[-n:]

# d) Sort the values in the matrix
sorted_matrix = np.sort(my_arr, axis=None).reshape(my_arr.shape)

print("Original array:\n", my_arr)
print("Indices of the sorted array:\n", sorted_indices)
print(f"{k} smallest values:\n", k_smallest_values)
print(f"{n} largest values:\n", n_largest_values)
print("Sorted matrix:\n", sorted_matrix)
 