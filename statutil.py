"""
Created on 6/14/2018

@author: Dylan Langone
"""

import matplotlib.pyplot as plt
import numpy as np
import pylab
import combinutil

def binom(x, n, p):
	"""
	Gives probability of x times occurring for event of probability p
	out of n trials
	"""
	return combinutil.choose(n, x)*p**x*(1-p)**(n-x)


