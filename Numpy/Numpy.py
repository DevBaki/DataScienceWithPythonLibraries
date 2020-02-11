# Welcome to Numpy Examples

# Arrays in NumPy: NumPy’s main object is the homogeneous multidimensional array.
#
#     It is a table of elements (usually numbers), all of the same type, indexed by a tuple of positive integers.
#     In NumPy dimensions are called axes. The number of axes is rank.
#     NumPy’s array class is called ndarray. It is also known by the alias array.

# Installation of Numpy                pip install numpy

import numpy as np  # import numpy

oneDimAxis = np.array([1, 2, 3])  # create one dimensional array

twoDimAxis = np.array([[1, 2, 3],  # create two dimensional array
                       [4, 5, 6]])

print(type(oneDimAxis))  # type of the element
print(type(twoDimAxis))

print('-------------------------------------------------------------------------------------')

print(oneDimAxis.shape)  # Number of elements in the array
print(twoDimAxis.shape)

print('-------------------------------------------------------------------------------------')

print(oneDimAxis.ndim)  # Number of dimension (here is 1)
print(twoDimAxis.ndim)

print('-------------------------------------------------------------------------------------')

print(oneDimAxis.size)  # Number of elements
print(twoDimAxis.size)

print('-------------------------------------------------------------------------------------')

floatArray = np.array([0.1, 0.2, 0.3])
print(oneDimAxis.dtype)  # Type of the elements in the array
print(floatArray.dtype)
print(oneDimAxis.itemsize)
print(floatArray.itemsize)
print(oneDimAxis.data)

print('-------------------------------------------------------------------------------------')

createArray = np.arange(25).reshape(5, 5)  # create array with dimension 5 and with elements 5
print(createArray)
print(createArray.shape)
print(createArray.itemsize)

print('-------------------------------------------------------------------------------------')

zerosArray = np.zeros((3, 5))  # creates the numpyArray with zeros
print(zerosArray)

print('-------------------------------------------------------------------------------------')

onesArray = np.ones((3, 5))  # creates the numpyArray with ones
print(onesArray)
print('-------------------------------------------------------------------------------------')
arrangeArray = np.arange(10, 50, 15)
arrangeArray1 = np.arange(0.1, 5, 0.8)
normalCreateArray = np.arange(6)
twoDimArrays = np.arange(24).reshape(2, 3, 4)

print(arrangeArray)
print(arrangeArray1)
print(normalCreateArray)
print(twoDimArrays)
print('-------------------------------------------------------------------------------------')

a = np.arange(1, 6, 1)  # create array which starts with 1 , increment by 1 until range 5
b = np.arange(2, 10, 2)  # create array which starts with 2 , increment by 2 until range 10
d = np.arange(3, 20, 4)
print(a)
print(b)
print(d)

# c = b - a                        # subtract array b from array a (could nt  do this operation because of different
# e = d - a                        # Subtract can be done
print(d - a)
# shapes )
# print(c)
print(b ** 2)
print(b > 5)
print('-------------------------------------------------------------------------------------')
print('will continue in Numpy2.py')
