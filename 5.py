import numpy as np
a=np.arange(21)
a[(a>=9)&(a<=15)] *=-1
print(a)