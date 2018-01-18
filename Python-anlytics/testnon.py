# -*- coding: utf-8 -*-
"""
Created on Thu Nov 09 15:16:42 2017

@author: ralall
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy import log as log

def func(x, a, b, c):
    return a * log(b * x) + c

x = np.array([0, 1.1029, 1.6148])
y = np.array([-8.5067, -6.8924, -6.713])

popt, pcov = curve_fit (func, x, y)

plt.figure()
plt.plot(x, y, 'k.', label = 'Raw Data')
plt.plot(x, func(x, *popt), 'k-', label = 'Fitted Curve')
plt.xlabel('ln(x)')
plt.ylabel('y')
plt.legend()
plt.show()