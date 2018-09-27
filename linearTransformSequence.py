'''

linearTransformSequence.py

Incorporates eigenvectors.py and cuttingSequence.py to generate the cutting sequences of the expanding eigenline
and an approximation vector that is repeatedly mapped by a hyperbolic matrix.

'''

#=== Import Statements ===#

import math
import numpy as np

import cuttingSequence as cutSeq
import eigenvectors as eig

#=== Constants ===#

WORD_LENGTH_MAX = 50 # Maximum number of terms in cutting sequence
MATRIX_APPLY_MAX = 15 # Number of times transformation matrix is applied to testVector
MATRIX_ELEMENT_MAX = 9 # max value of elements in randomly-generated hyperbolic matrix

#=== Variables ===#

matrix = eig.genMatrix(MATRIX_ELEMENT_MAX) # randomly generated hyperbolic matrix

expandingEigen = eig.eigenHyp(matrix) # expanding eigenvector of matrix
slope = eig.slope(expandingEigen) # slope of expanding eigenvector

testVector = np.matrix('1; 1') # Initial comparison integer vector

seq = "" # used for storing the cutting sequence of a given line

#=== Function Definitions ===#
'''
Generates a list of approximation vectors by iterating the application of the hyperbolic matrix onto an integer vector <1,1>

@param:
- initVector: the initial integer vector being tested
- matrix: the hyperbolic matrix iteratively applied to "initVector" MATRIX_APPLY_MAX times,
recording each resulting vector as an iteration

@return: generates a list of approximation vectors 
'''
def approxVectors(initVector, matrix):
	
	returnList = []
	iterVector = np.matrix([[initVector.item(0)], [initVector.item(1)]])
	
	for i in range(0,MATRIX_APPLY_MAX):
		returnList.append(iterVector)
		iterVector = matrix.dot(iterVector)
	
	return returnList

'''
Generates a list of the slopes of the approximation vectors that corresponds to the list of approximation vectors

@param:
- approxVectorList: list of vectors resulting from the repeated application of "matrix" onto a "testVector"

@return: list of the slopes of the approximation vectors
'''
def approxSlopes(approxVectorList):
	returnList = []
	for i in approxVectorList:
# 		print i
		returnList.append(eig.slope(i))
	return returnList

'''
Generates a list of the cutting sequences of the approximation vectors
that corresponds to the list of the slopes of the approximation vectors

@param:
- approxSlopeList: list of slopes of vectors resulting from the repeated application of "matrix" onto a "testVector"

@return: list of the cutting sequences of the approximation vectors
'''
def approxSequences(approxSlopeList):
	returnList = []
	for i in approxSlopeList:
		seq = ""
# 		print i
		returnList.append(cutSeq.cuttingSeq(i, WORD_LENGTH_MAX, seq, 1, 1))
	return returnList

#=== Function Executions ===#

approxVectorList = approxVectors(testVector,matrix)
approxSlopeList = approxSlopes(approxVectorList)

# print approxVectorList
print "Hyperbolic Matrix: " + str(matrix)
print "\n"

print "Eigenvector Tested: {0}".format(expandingEigen)
print "\n"

print "Eigenvector Slope: {0}".format(slope)
print "\n"

print "Slope list: \n {0}".format(approxSlopeList)
print "\n"

print "Sequence List: \n {0}".format(approxSequences(approxSlopeList))

'''
Direct determination of cutting sequence of eigenline.
Note that that absolute value of the slope is taken so that, should "slope" be negative, the cutting sequence can still be generated.
Taking the absolute value of the slope does not affect its cutting sequence because the square grid is reflected along the x-axis.
Therefore, the cutting sequence is identical between two slopes that are negatives of one antoher.
'''
print "Expanding Eigenvector Cutting Sequence: \n"
print cutSeq.cuttingSeq(1.0*abs(slope), WORD_LENGTH_MAX, seq, 1, 1)