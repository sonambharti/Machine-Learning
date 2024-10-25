# NumPy Introduction
NumPy is a library for the Python programming language, adding support for large, multi-dimensional arrays and
matrices, along with a large collection of high-level mathematical functions to operate on these arrays.
NumPy arrays are similar to Python lists, but they are more efficient and offer more features.

## Methods of NumPy
### 1. numpy.array()
    -   The numpy.array() function is used to create a NumPy array from a Python list or other iterable
    -   It can also be used to create an array from a Python scalar value.

**Features** <br/>
1.  **NumPy Arrays**: NumPy arrays are the core data structure in NumPy.
2.  **Vectorized Operations**: NumPy arrays support vectorized operations, which means that operations
can be performed on the entire array at once, rather than having to iterate over each element individually
3.  **Broadcasting**: NumPy arrays support broadcasting, which allows you to perform operations on
arrays with different shapes and sizes.

**Advantages** of Numpy arrays over Python Lists:<br/>
1. It consumes less memory.
2. It is faster than Python lists.
3. It supports vectorized operations.
4. It is convenient to use.


### 3. Indexing and Slicing of a numpy array
    -   Indexing: It is used to access a single element of an array.
    -   Slicing: It is used to access a subset of elements in an array.
    -   Array Indexing and Slicing is similar to Python List Indexing and Slicing.
    -   Array Indexing and Slicing can be done using square brackets [] and colon : respectively
    -   Array Indexing and Slicing can be done using negative index as well.

**Examples** <br/>
````
import numpy
arr = numpy.array([1,2,3])
print(arr[0]) # indexing
print(arr[1:3]) # slicing
````

### 3. Data Type of a numpy array
    -   The data type of a numpy array can be specified when creating the array using the numpy
    -   The data type of a numpy array can also be changed after the array is created using
    -   The data type of a numpy array can be checked using the numpy `dtype` function.

**Example** <br/>
````
import numpy
arr = numpy.array([1,2,3], dtype=numpy.int32)
print(arr.dtype) # checking data type
````

### 4. numpy.reshape()
    -   The numpy.reshape() function is used to change the shape of a numpy array without changing
    -   The numpy.reshape() function can be used to change the shape of a numpy array from

**Examples** <br/>
````
import numpy
arr = numpy.array([1,2,3,4])
arr = arr.reshape(2,2)
````

### 5. numpy.transpose()
    -   The numpy.transpose() function can be used to reverse or swap the order of the axes

**Examples** <br/>
````
arr = numpy.array([1,2], [3,4])
arr = numpy.transpose(arr)

````


