#! /usr/bin/env python

import numpy as np
from __init__ import DO

n_data = 5000
n_calc = 500
x = np.random.rand(n_data)
y = np.random.rand(n_data+100)
targets = np.random.randint(2, size=n_data)

# DO calculated without statistics
print(DO(fx=x, gx=y, target=targets))

# DO calculated with statistics (i.e. mean and stdev of DO)
print(DO(fx=x, gx=y, target=targets, stats=True))

# DO example where you expect perfect similarity (i.e. compare x with x)
print(DO(fx=x, gx=x, target=targets, n_data=n_calc))
print(DO(fx=x, gx=x, target=targets, n_data=n_calc, stats=True, boot_loops=20))