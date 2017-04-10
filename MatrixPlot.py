# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 18:37:30 2017

@author: jiaqi
"""

import numpy as np
import matplotlib.pyplot as plt

matrix = np.random.random((10, 10, 3))

fig, ax = plt.subplots(1,3, figsize=(12, 3))
plt.subplots_adjust(left=0.05, right=0.85)
for i in range(3):
    im = ax[i].imshow(matrix[:, :, i], interpolation='nearest')
    ax[i].set_aspect("equal")

plt.draw()
p = ax[-1].get_position().get_points().flatten()
ax_cbar = fig.add_axes([0.9,p[1], 0.02, p[3]-p[1]] )
plt.colorbar(im, cax=ax_cbar)

plt.show()