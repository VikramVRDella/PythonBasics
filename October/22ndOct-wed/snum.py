print(
    '''
    ***************
    * Numpy Array *
    ***************
    '''
)

import numpy as np
a=np.array([1, 2, 3, 4, 5])
print(a) 
print(type(a))
print("\n")
print("Dimensional Arrays...")
b=np.array(32)
c=np.array([1,2,3,4,5])
d=np.array([[1,2,3],[4,5,6]])
e=np.array([[[1,2,4],[2,4,5]],[[1,4,3],[3,5,2]]])
print(b.ndim)
print(c.ndim)
print(d.ndim)
print(e.ndim)
