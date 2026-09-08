#task 1 Numpy
import numpy as np
arr = np.arange(1,11)
arr2D = np.arange(1,10).reshape(3,3)
temp_list = [10,20,30,40,50]
converted_arr = np.array(temp_list)
print(arr.shape, arr2D.shape,converted_arr.shape,'The Shapes of All Array')
print(arr.dtype, arr2D.dtype,converted_arr.dtype,'The Data Type Each Arrays')
#optional
print(arr,'\n',arr2D,'\n',converted_arr)