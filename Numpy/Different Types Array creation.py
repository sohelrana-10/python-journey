import numpy as np

zero_arr=np.zeros((3,3))
print(zero_arr)

one_arr=np.ones((2,2))
print(one_arr)

# empty_arr=np.empty((4,4))
# print(empty_arr)

num_arr=np.array((3,3))
print(num_arr)

#sequential array

seq_arr=np.arange(1,13)
print(seq_arr)

#from arange to reshape to form 2D array

reshape_arr=seq_arr.reshape(2,3,2)
print(reshape_arr)