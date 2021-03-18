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

# NaN
array2 = array2.astype('float')  # need to convert to float. Int type var could not assigned as Nan
array2[1, 2] = np.nan
array2[0, 1] = np.inf
print(array2)

index = np.where(np.isinf(array2)) or np.where(np.isnan(array2))  # bool type is not right
print('index: %d', index)
array2[index] = 666
print(array2)

index = np.isnan(array2) | np.isinf(array2)
print('index: %d', index)
array2[index] = 666
print(array2)

array2[array2 == 666] = 0
print(array2)
print('The mean value is: ', array2.mean())
print("The max value is: ", array2.max())
print('The min value is: ', array2.min())

print('max value of each column: ', array2.max(axis=0))
print('min value of each row: ', array2.min(axis=1))

# numpy copy
array2_copy = array2[:, 1:]  # shallow copy
print(array2_copy)
array2_copy[:1, :1] = 1
array2_copy[1, 1] = 8
print(array2)

array2[array2 == 1] = 0
array2_copy = array2[:, 1:].copy()  # deep copy
array2_copy[:1, :1] = 666
print(array2_copy)
print(array2)

# reshape and flatten
print(array2.shape)
array2 = array2.reshape(3, 2)
print(array2)
print(array2.shape)

array2_ravel_result = array2.ravel()
print("array2_ravel_result: ", array2_ravel_result)
a = array2_ravel_result[0]
array2_ravel_result[0] = 666
print(array2)  # change orig data --> shallow copy
array2_ravel_result[0] = a

array2_flatten_result = array2.flatten()
print("array2_flatten_result: ", array2_flatten_result)
array2_flatten_result[0] = 666
print(array2)  # does not hurt orig data --> deep copy

# series, range
a = np.arange(9)
print(a)

a = np.linspace(0, 10, 5)
print(a)

a = np.logspace(1, 10, num=10, base=10)
print(a)

a = np.array([1, 2, 3])
print(a)

# tile is repeat whole array
tile_a = np.tile(a, 2)
print(tile_a)

repeat_a = np.repeat(a, 2)
print(repeat_a)

# unique / count
a = np.array(['cat', 'cat', 'dog', 'sheep', 'dog'])
print(np.unique(a))
print(np.unique(a, return_counts=True))

# random
np.random.seed(19)
print(np.random.randn(3, 3))  # rand'n' --> last n means normalized
print(np.random.rand(3, 3))  # uniform distribution

# cat, dog, sheep
print(np.random.choice(['cat', 'dog', 'sheep'], size=10))
print(np.random.choice(['cat', 'dog', 'sheep'], size=10, p=[0.3, 0.45, 0.25]))

a = np.arange(4).reshape(2, 2)
b = np.arange(6, 10).reshape(2, 2)
print(a)
print(b)

c = np.concatenate([a, b], axis=0)  # axis = 0, vertical
print(c)
print(c.shape)
d = np.concatenate([a, b], axis=1)  # axis = 1, horizontal
print(d)
print(d.shape)


# vectorize
def myFunc(x):
    if x % 2 == 0:
        return x / 2
    else:
        return x ** 2


a = np.array([1, 2, 3])

print(myFunc(2))
print(myFunc(5))
# print(myFunc(a)) # error --> a is array, not a number
myFunc_v = np.vectorize(myFunc)
print(myFunc_v(a))  # now myFunc could process array

a = np.arange(6).reshape(2, 3)
print(a)


def func(x):
    return (max(x) - min(x)) / 2


print(np.apply_along_axis(func, 0, a))
print(np.apply_along_axis(func, 1, a))
