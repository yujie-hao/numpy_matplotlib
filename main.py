import numpy as np

# numpy
list1 = [0, 1, 2, 3, 4, 5]
array1 = np.array(list1)
type(array1)

# list1 + 2 # list could not add 2 --> TypeError: can only concatenate list (not "int") to list
array1 = array1 + 2  # vectorized array
print(array1)

list2 = [[0, 1, 2], [3, 4, 5]]
array2 = np.array(list2)
print(array2)

array2 = np.array(list2, dtype='float')
print(array2)

array2 = array2.astype('int')
print(array2)

print('shape is: ', array2.shape)
print('size is: ', array2.size)
print('dtype is: ', array2.dtype)
print('dimension is: ', array2.ndim)  # interesting

print(array2[:2, :2])
print(array2 % 2 == 0)

# index
print(array2[array2 % 2 == 0])
a = np.arange(9)  #
print(a)
print(np.where(a % 2 == 0))
print(a[np.where(a % 2 == 0)])
