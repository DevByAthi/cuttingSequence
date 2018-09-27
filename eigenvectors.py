'''
eigenvectors.py

Takes a given matrix, checks that it is hyperbolic, and returns the expanding eigenvector and its slope

'''

import numpy as np
import math
from random import *

#=== Function Definitions ===#

'''
tests if a given matrix has a determinant of 1
'''
def detTest(matrix):
	print round(np.linalg.det(matrix)) == 1

'''
tests if a given matrix is hyperbolic (i.e. has determinant of 1 and a trace whose absolute value is greater than 2)
'''
def isHyperbolic(matrix):
	if np.trace(matrix) > 2 and round(np.linalg.det(matrix)) == 1:
		return True;
	return False;

'''

@param:
- matrix: 2-by-2 matrix with real entries

@return: returns the eigenvector of the given hyperbolic matrix whose slope is positive
'''
def eigenHyp(matrix):
	
	list = []
	
	if isHyperbolic(matrix):
		w, v = np.linalg.eig(matrix)
		
		largestEigenvalue = 0
		termOfLargest = -1
		
		for i in range(len(v)):
				# print i
# 				print "Eigenvalue for (0): {1}".format(i, w[i])
# 				print "Eigenvector for (0): {1}, with slope {2}".format(i, v[i], slope(v[i]))
				# if slope(v[i]) > 0:
# 					return v[i]
				if abs(w[i]) > abs(largestEigenvalue):
					largestEigenvalue = w[i]
					termOfLargest = i
		
		return v[termOfLargest]

'''
Determines slope of a 2-by-1 vector (which can encode the slope of a line crossing through it)

@return: returns slope of given vector
'''
def slope(vector):
	return (1.0*vector.item(1))/vector.item(0);


'''
Randomly generates a hyperbolic matrix, checking that the matrix formed is hyperbolic

@return: returns a random hyperbolic matrix with elements of value "> 0" and "< max"
'''
def genMatrix(max):
	
	# initialize
	a = randint(0,max)
	b = 0
	c = 0
	d = randint(0,max)
	
	while abs(a+d) <= 2:
		d = randint(0,max)
	

	bc = (a*d) - 1
	
	if a == 0 or d == 0:
		b = 1
		c = -1
	else:
		if isPrime(bc):
			b = bc
			c = 1
		else:
			b = randFactor(bc)
			c = bc/b
	retMatrix = np.matrix([[a, b], [c, d]])
	
	if isHyperbolic(retMatrix):
		return retMatrix

'''
Checks if an integer is prime. Speeds up calculations in determining 'b' and 'c' in the genMatrix() function

@param:
- num (integer): an integer input

@return: a boolean stating whether "num" is prime
'''
def isPrime(num):
	
	if num < 2:
		return False;
	
	for i in range(2,num):
		if num % i == 0:
			return False;
	
	return True;

'''
Returns a random factor of a given integer.
Speeds up calculations in determining 'b' and 'c' in the genMatrix() function, should b*c not be prime

@param:
- num (integer): an integer input

@return: a random factor of "num"
'''
def randFactor(num):
	if isPrime(num):
		return 1
	
	list = []
	
	for i in range(2,num):
		if num % i == 0:
			list.append(i)
	
	return list[randint(0,len(list) - 1)]