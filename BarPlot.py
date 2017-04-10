# -*- coding: utf-8 -*-
"""
Created on Sun Apr  9 21:47:12 2017

@author: jiaqi
"""

import matplotlib.pyplot as plt
import matplotlib
matplotlib.style.use('ggplot')
import pandas as pd

ix3 = pd.MultiIndex.from_arrays([['a', 'a', 'a', 'a', 'b', 'b', 'b', 'b'], ['foo', 'foo', 'bar', 'bar', 'foo', 'foo', 'bar', 'bar']], names=['letter', 'word'])
df3 = pd.DataFrame({'data1': [3, 2, 4, 3, 2, 4, 3, 2], 'data2': [6, 5, 7, 5, 4, 5, 6, 5]}, index=ix3)

# Group by index labels and take the means and standard deviations for each group
gp3 = df3.groupby(level=('letter', 'word'))

means = gp3.mean()
errors = gp3.std()
fig, ax = plt.subplots(figsize=[12,9])
means.plot.bar(yerr=errors, ax=ax)