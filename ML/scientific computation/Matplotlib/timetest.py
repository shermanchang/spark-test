import numpy as np
import math
from time import time

x = np.arange(1,10,1)
y = np.sin(x)

x = [i*0.001 for i in xrange(1000000)]
start = time()
for i,t in enumerate(x):
    x[i] = math.sin(t)


print "== python =="
print x
print time() - start

x = [i*0.001 for i in xrange(1000000)]
x = np.array(x)
start = time()
ar = np.sin(x, x)


print "== numpy =="
print ar
print time() - start
