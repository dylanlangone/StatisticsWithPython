"""
Created on 6/14/2018

@author: Dylan Langone
"""

import matplotlib.pyplot as plt
import numpy as np
import pylab
import combinutil
import math

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
	
def multinom3(x1, x2, x3, p1, p2, p3):
	if (p1 < 0 or p2 < 0 or p3 < 0 or (((p1 + p2 + p3) - 1) > .0000001)):
		raise ValueError("Enter a probability from 0 to 1")
		
	if (x1 + x2 + x3 != n):
		raise ValueError("Enter valid numbers of successes")
		
	return math.factorial(n)/(math.factorial(x1)*math.factorial(x2)*math.factorial(x3))*p1**x1*p1**x2*p3**x3


