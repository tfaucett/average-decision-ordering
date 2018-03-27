#! /usr/bin/env python

import numpy as np
from __init__ import DO

n_data = 5000
n_calc = 500
x = np.random.rand(n_data)
y = np.random.rand(n_data)
targets = np.random.randint(2, size=n_data)

''' DO calculated without statistics '''
print(DO(fx=x, gx=y, target=targets, n_data=n_calc))

''' DO calculated with statistics (i.e. mean and stdev of DO) '''
print(DO(fx=x, gx=y, target=targets, n_data=n_calc, stats=True))