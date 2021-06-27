'''import numpy as np
a= np.array([[1,2],[1,4],[1,68]])
print(a)
print("maximum value is ",np.max())
'''


'''
import numpy as np 
mat=np.array([[1,6,5],[3,4,8],[2,12,3]])
mm_list=mat.tolist()
print("list is",mm_list)
'''
'''
import numpy as np
a=np.arange(9).reshape(3,3)
print("original matrix is \n",a)
m=np.trace(a)
print("sum of diagonal elements is " ,m)
'''
'''
import numpy as np 
matrix1=([1,6,5],[3,4,8])
matrix2=([3,4,6],[5,6,7])
res=np.multiply(matrix1,matrix2)
print(res)'''
'''
import numpy as np
from numpy.lib.arraysetops import unique
arr=np.array([10,20,5,10,8,20,8,9])
Unique ,frequency=np.unique(arr,return_counts=True)
print("Unique elements ",Unique)
print("Frequency  is ",frequency)
'''