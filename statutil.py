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
	if (p > 1 or p < 0):
		raise ValueError("Enter a probability from 0 to 1")
	
	if (x < 0):
		raise ValueError("Enter a valid number of successes")
		
	if (x > n):
		raise ValueError("Make sure number of successes is less than or equal to number of trials");
		
	return combinutil.choose(n, x)*p**x*(1-p)**(n-x)


