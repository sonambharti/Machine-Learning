import numpy

arr = numpy.array([1,2,3,4])
print("Shape of array - ", arr.shape)
print(arr[0]) # indexing
print(arr[1:3]) # slicing
arr = arr.reshape(2,2)
print("New array: ", arr)
print(arr.dtype) # checking data type
print("Shape of array = ", arr.shape)
print("Dimension of new array = ", arr.ndim)

arr = numpy.transpose(arr)
print("Transpose: ", arr) # Transpose of array

# Copy of the numpy array
arr_copy = numpy.copy(arr)
arr[0][1] = 7
print("Copy of the array: ", arr_copy)

# view of the numpy array
arr_view = arr.view()
print("arr_view: ", arr_view)

arr[1][1] = 6
print("arr : ", arr)
print("arr_view: ", arr_view)

