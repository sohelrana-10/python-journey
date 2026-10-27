import numpy as np

# mylist=[i for i in range(1,101)]
# arr=np.array(mylist)
# print(arr)
# print("Dimension of your numpy array is:",arr.ndim)

mylist = [[j for j in range(3)] for i in range(3)]
print(mylist)

arr = np.array(mylist)
print(arr)
print("Number of dimensions:", arr.ndim)
print("Shape of your array:",arr.shape)
