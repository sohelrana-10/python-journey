import numpy as np

# arr=np.array([[1,2,3,0],
#               [4,5,6,-1]])
# idx=np.where(arr==3)
# print(idx)
#Sort the element:
# arr.sort()
# print(arr)

#Search the element


# import numpy as np

# my_arr = np.array([1, 23, 5, 2, 6, 9])

# print("The index of all 2:", np.where(my_arr == 2))

import numpy as np

my_arr = np.array([1, 2, 3, 4, 5, 5, 5, 5, 5, 58, 6, 9])

# Find where 4 would be inserted in a sorted version
idx = np.searchsorted(np.sort(my_arr), 4)
print("Insert position for 4:", idx)

# Now actually insert 100 into the original array at index 2
new_arr = np.insert(my_arr, 2, 100)
print(new_arr)
