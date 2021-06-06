
import numpy as np
a = np.array([[1, 2, 3, 4, 5],[1, 2, 3, 4, 5]])
print(a.ndim)
print(a[0,0])

arr = np.array([1,2,3,4,5,6,7])
arr2 = np.array([1,2,3,4,5,6,7])


print(arr[2:-2])
print(arr[3:])
print(arr[::2])

print(arr.dtype)


arr_flot = np.array([1,2,3,4,5,6,7],dtype="float")
print(arr_flot)

print(arr_flot.shape)
print(a.shape)

arr3 = np.concatenate((arr,arr2))
print(arr3)

# print(np.array_split(arr3,25))

print("hi",np.where(arr3 == 1))

print(np.sort(arr3))

print(np.random.randint(0,100))

print(test = np.random.normal(size=1000,loc=50,scale=0.2))
test = np.random.normal(size=1000,loc=50,scale=0.2)
print(arr3.cumsum())

print(np.add(arr,arr2))
print(np.subtract(arr,arr2))