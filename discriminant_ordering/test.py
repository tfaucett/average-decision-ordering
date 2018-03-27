#! /usr/bin/env python

import numpy as np
from __init__ import DO

n_data = 100
x = np.random.rand(n_data)
y = np.random.rand(n_data)
targets = np.random.randint(2, size=n_data)

print(DO(fx=x, gx=y, target=targets, n_data=n_data))
print(DO(fx=x, gx=y, target=targets, n_data=n_data, stats=True))