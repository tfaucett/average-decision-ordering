#! /usr/bin/env python

import numpy as np
from __init__ import DO

x = np.random.rand(10)
y = np.random.rand(10)
targets = np.random.randint(2, size=10)

print(DO(x, y, targets, 10))