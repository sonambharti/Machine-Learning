import numpy

arr = numpy.array([1,2,3,4])
print(arr[0]) # indexing
print(arr[1:3]) # slicing
print(arr.dtype) # checking data type
arr = arr.reshape(2,2)
print("shape of array = ", arr.shape)
print("New array: ", arr)