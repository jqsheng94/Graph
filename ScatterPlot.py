# -*- coding: utf-8 -*-
"""
Created on Sun Apr  9 22:41:28 2017

@author: jiaqi
"""

import numpy as np
import matplotlib.pyplot as plt


N = 50
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)
area = np.pi * (15 * np.random.rand(N))**2  # 0 to 15 point radii

plt.figure(figsize=[12,9])
plt.scatter(x, y, s=area, c=colors, alpha=0.5)
plt.show()