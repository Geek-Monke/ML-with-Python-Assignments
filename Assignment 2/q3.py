import numpy as np
my_arr = np.ones((5, 5))
print("5x5 Array filled with ones:\n", my_arr)

value = my_arr[3, 1]
print("Value at fourth row and second column:", value)

slice_arr = my_arr[0:3, 1:3]
print("Slice array (rows 0-2, columns 1-2):\n", slice_arr)

slice_arr = my_arr[-3:, :]
print("Slice with all columns of the last 3 rows:\n", slice_arr)

slice_arr = my_arr[-3:, :]
slice_arr[:] = -1
print("Slice array after assigning -1 to the last 3 rows:\n", slice_arr)
