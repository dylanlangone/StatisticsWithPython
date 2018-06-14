"""
Created on 6/14/2018

@author: Dylan Langone
"""

import matplotlib.pyplot as plt
import numpy as np
import pylab
import math

def choose(n, r):
	return math.factorial(n)/(math.factorial(r)*math.factorial(n-r))