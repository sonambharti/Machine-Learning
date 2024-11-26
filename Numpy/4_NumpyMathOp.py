import numpy as np

a = np.arange(0,18).reshape((6, 3))
b = np.arange(20,38).reshape((6, 3))
print(a)
print(b)

# print("Addition: \n", np.add(a, b))
# print("Subtraction: \n", np.subtract(a, b))
# print("Multiply: \n", np.multiply(a, b)) # Note: This is not a matrix multiplication

# Matrix Multiplication
b = b.reshape((3, 6))
print(f"Reshaped b {b.shape} : \n{b}")
# print("Matrix Multiplication: \n", a@b) # `@` is used for matrix multiplication
# print("Matrix Multiplication: \n", a.dot(b))

print("Maximum Element in b: ",b.max())
print("Minimum Element in b: ",b.min())
print("Index of Maximum Element in b: ",b.argmax())
print("Sum all the elements in b: ",np.sum(b))

# sum of all elements via axis
print("Sum of b in axis = 1 \n", np.sum(b, axis=1))
print("Sum of b in axis = 0 \n", np.sum(b, axis=0))

# mean of all the element of given array
print("Mean of all the element of given array: ", np.mean(b))

# sqrt of the each element of the given array
print("sqrt of the each element of the given array: \n", np.sqrt(b))


# standard deviation of all the element of given array
print("standard deviation of the all element of given array: ", np.std(b))


# Log of all the element of given array
print("Log of the all element of given array: ", np.log(b))
