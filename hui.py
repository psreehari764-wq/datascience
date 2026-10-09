import numpy as np
from psutil import swap_memory

a=np.array([[1,2,3],[2,3,4],[3,4,5]])
num=a[[-1,1,0]]
print(num)