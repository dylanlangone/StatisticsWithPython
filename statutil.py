"""
Created on 6/14/2018

@author: Dylan Langone
"""

import matplotlib.pyplot as plt
import numpy as np
import pylab
import combinutil as cu
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
		
	return cu.choose(n, x)*p**x*(1-p)**(n-x)
	
def multinom3(x1, x2, x3, p1, p2, p3):
	if (p1 < 0 or p2 < 0 or p3 < 0 or (((p1 + p2 + p3) - 1) > .0000001)):
		raise ValueError("Enter a probability from 0 to 1")
		
	if (x1 + x2 + x3 != n):
		raise ValueError("Enter valid numbers of successes")
		
	return math.factorial(n)/(math.factorial(x1)*math.factorial(x2)*math.factorial(x3))*p1**x1*p1**x2*p3**x3
	
def multinom4(x1, x2, x3, x4, p1, p2, p3, p4):
	if (p1 < 0 or p2 < 0 or p3 < 0 or p4 < 0 (((p1 + p2 + p3 + p4) - 1) > .0000001)):
		raise ValueError("Enter a probability from 0 to 1")
		
	if (x1 + x2 + x3 + x4 != n):
		raise ValueError("Enter valid numbers of successes")
		
	return math.factorial(n)/(math.factorial(x1)*math.factorial(x2)*math.factorial(x3)*math.factorial(x4)*p1**x1*p1**x2*p3**x3*p4**x4
	
def hypgeo(x, N, n, k):
	"""returns probability of x successes of sample size n 
	of total N with k elements of N that are possible successes"""
	
	if (n > N or k > N or x > N or x > n or x > k)
		raise ValueError("Inappropriate arguments")
	return cu.choose(k, x)*cu.choose(N-k,n-x)/cu.choose(N,n)
	
def negbionom(x, k, p):
	"""returns probability of kth success occurring on xth trial of event of probability p"""
	if (k > x or p < 0 or p > 1 or x <= 0 or k <= 0)
		raise ValueError("Inappropriate arguments")
	return cu.choose(x - 1, k - 1)*p**k*(1-p)**(x-k)
	
def poisson(x, l, t):
	"""returns Poisson probability of x occurring"""
	if (x < 0 or l < 0 or t < 0)
		raise ValueError("Inappropriate arguments")
	
	return math.exp(-1*l*t)*(l*t)**x/(math.factorial(x))


