import numpy

arr = numpy.array([1,2,3,4])
print("Shape of array - ", arr.shape)
print(arr[0]) # indexing
print(arr[1:3]) # slicing
print(arr.dtype) # checking data type
print("Shape of Transpose array = ", arr.shape)
arr = arr.reshape(2,2)
print("New array: ", arr)
arr = numpy.transpose(arr)
print("Transpose: ", arr) # Transpose of array
print("Shape of array = ", arr.shape)
