#! /usr/bin/env python

import numpy as np
from __init__ import DO

x = np.random.rand(100)
y = np.random.rand(100)
targets = np.random.randint(2, size=100)

print(DO(x, y, targets, 100))