import numpy as np
from scipy import stats

speed=[97,76,234,54,143,65,134,46,124]

x=np.mean(speed)
y=np.median(speed)
z=stats.mode(speed)
a=np.std(speed)
b=np.var(speed)
print(x)
print(y)
print(z)
print(a)
print(b)