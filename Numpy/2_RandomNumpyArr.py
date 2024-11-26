import numpy as np

# rand() - generate random value between 0 to 1
randArr1 = np.random.rand(4)
print("1-D random array: \n", randArr1)

randArr2 = np.random.rand(4,3)
print("2-D random array: \n", randArr2)

# randn() - generate random value close to zero, either positive or negative.
randnArr1 = np.random.randn(4)
print("1-D random array: \n", randnArr1)

randnArr2 = np.random.randn(2,4)
print("2-D random array: \n", randnArr2)


# ranf() - generate random float value in the half open interval[0.0, 1.0)
randfArr1 = np.random.ranf(4)
print("1-D random array: \n", randfArr1)

# randfArr2 = np.random.ranf(2,4)
# print("2-D random array: \n", randfArr2)

# randint() - generate a random array between a range
randintArr1 = np.random.randint(4)
print("1-D random array: \n", randArr1)

randintArr2 = np.random.randint((4,3))
print("2-D random array: \n", randintArr2)
