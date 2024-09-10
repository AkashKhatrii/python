import numpy as np

arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([[4], [5], [6], [7]])
arr3 = np.array([4, 5, 6, 7])

arr1_multiply_arr2 = arr1 * arr2
arr1_plus_arr3 = arr1 + arr3

arr_zeros = np.zeros((5, 3))
arr_ones = np.ones((5, 4))

arr_range = np.arange(7,)
arr_linspace = np.linspace(1, 5, 3) # 3 evenly space numbers between 1 and 5

print(arr1)
print(arr2)
print(arr1_multiply_arr2)
print(arr1_plus_arr3)
print(arr_zeros)
print(arr_ones)
print(arr_range)
print(arr_linspace)

print("ARRAY ATTRIBUTES")
print(f"arr1 shape: {arr1.shape}")

print("MULTI DIMENSIONAL SLICING")
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr[:2, 1:3])

print("SLICING USING INTEGERS")
arr = np.array([10, 20, 30, 40, 50])
print(arr[[0, 2, 4]])  # Output: [10, 30, 50]

print('\n\n')
print("ARRAY OPS")
arr = np.array([1, 2, 3])
print(arr)
print(arr + 1)  # Output: [2, 3, 4]
print(arr * 2)  # Output: [2, 4, 6]

print('\n\n')
print("MATHEMATICAL FUNCTIONS")
arr = np.array([1, 2, 3])
print(arr)
print(np.sqrt(arr))  # Output: [1. , 1.414, 1.732]
print(np.sin(arr)) 


arr = np.array([1, 2, 3, 4])
print(np.sum(arr))    # Output: 10
print(np.mean(arr))   # Output: 2.5
print(np.max(arr))    # Output: 4
print(np.min(arr))
print(np.std(arr))

print('\n\n')
print("RANDOM NUMBERS")
print(np.random.rand())
print(np.random.randint(1, 10))
print(np.random.randint(1, 10, size=(2, 2)))  # 2x2 matrix of random ints from 1 to 9

print('\n\n')
print('RESHAPING ARRAYS')

arr = np.arange(6).reshape((2, -1))
print(arr)  
