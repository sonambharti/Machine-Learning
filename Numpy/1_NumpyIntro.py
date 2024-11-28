# %timeit [j**4 for j in range(1, 9)] # checking time to execute this line

import numpy as np
arr = np.arange(1,9) # creates an array of range 1 to 8
print("Initialized Array = ", arr)

# %timeit np.arange(1,9)**4

print("array of square of natural nos.: ", np.arange(1,6)**2)

print("Type of array: ", type(arr))


# Zeros Array
zeroArr1 = np.zeros(4) # creating 1-D array
print("Zero Array = ", zeroArr1)

zeroArr2 = np.zeros((3,4)) # creating 2-dimensional array
print("Two dimensional Zero Array :\n", zeroArr2)
print("Dimension of zeroArr2 = ", zeroArr2.ndim) # find Dimension of the array
print("Shape of the arr: ", zeroArr2.shape) # Shape of the array

zeroArr3 = np.zeros((3,4,4)) # creating 2-dimensional array
print("Multi dimensional Zero Array :\n", zeroArr3)
print("Dimension of zeroArr2 = ", zeroArr3.ndim) # find Dimension of the array
print("Shape of the arr: ", zeroArr3.shape) # Shape of the array

# Ones Array
oneArr1 = np.ones(4) # creating 1-D array
print("One Array = ", oneArr1)

oneArr2 = np.ones((3,4)) # creating 2-dimensional array
print("Two dimensional one Array :\n", oneArr2)
print("Dimension of oneArr2 = ", oneArr2.ndim) # find Dimension of the array
print("Shape of the arr: ", oneArr2.shape) # Shape of the array

oneArr3 = np.ones((4,4,4)) # creating multi-dimensional array
print("Multi dimensional one Array :\n", oneArr3)
print("Dimension of oneArr2 = ", oneArr3.ndim) # find Dimension of the array
print("Shape of the arr: ", oneArr3.shape) # Shape of the array

# Empty Array
emptyArr1 = np.empty(4) # creating 1-D array
print("Empty Array = ", emptyArr1)

# Full Array
fullArr1 = np.full(4, 5) # creating 1-D array
print("Full Array = ", fullArr1)

fullArr2 = np.full((3, 4), 7)  # creating 2-D array
print("Two Dimensional Full Array \n:", fullArr2)

# fullArr3 = np.full((3, 2), [1, 2, 3], [8, 4, 3])
# print("Muti dimensional full array with different values: ", fullArr3)

# Diagonal Array
diagonalArr1 = np.eye(3)
print("1 D Diagonal array: \n", diagonalArr1)

diagonalArr2 = np.eye(3, 3)
print("2 D Diagonal array: \n", diagonalArr2)

# Linespace Array
arr_lin1 = np.linspace(1,10, num=5)
print("Line array from 1 to 10 having 5 elements in it: ", arr_lin1)


arr_lin2 = np.linspace(0, 20, 5)
print("Line array from 0 to 20 having 5 elements in it: ", arr_lin2)
