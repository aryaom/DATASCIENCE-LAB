import numpy as np
m1=np.array([[[2,0,1],[3,6,2],[5,2,1]]])
m2=np.array([[[5,0,1],[1,2,3],[6,3,5]]])
print("Original 3-D matrix")
print(m1)
print(m2)
print("outer product of matrix")
r=np.outer(m1,m2)
print(r)
