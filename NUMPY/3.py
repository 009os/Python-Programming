
#Create an numpy array of all the even integers from 10 to 50.

import numpy as np
x = np.arange(10,51)
y = (x%2 == 0)
z = x[y]
print(z)
