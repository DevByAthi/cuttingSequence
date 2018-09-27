'''
Generates a cutting sequence for a line with a given slope.

NOTE: This program assumes that the line passes through the origin, hence why there is no input for the y-intercept.
Such a consideration is not pertinent to the theoretical component of the Paper.

'''

import math

# RECURSIVE PROCESS

# Take vector <1,1> (whose slope is 1) and compare to the given v's slope
#	If v's slope is less than that of <1,1>, then compare to <2,1>; Record vertical side being struck by ball
# 	If v's slope is greater than that of <1,1>, then compare to <1,2>; Record horizontal side being struck by ball
# Repeat process with successively better linear approximations

'''

Compares slope of given vector to a set of approximation vectors (with integer components)
and outputs the cutting sequence for a line along the given vector

Encoding:
Horizontal side intersected, "A"
Vertical side intersected, "B"

@param:
	- input_slope (float): slope of input line
	- iter (int): iterations of program remaining (to avoid an endless loop)
	- sequence (string): encodes the cutting sequence of a line with slope = "input_slope". sequence 
	is concatenated at each iteration of the function
	- comp_x: the x-component of the comparison integer vector used to determine whether
	the line with "input_slope" intersects a horizontal or vertical line. Increments if vertical side is hit.
	- comp_y:  the y-component of the comparison integer vector used to determine whether
	the line with "input_slope" intersects a horizontal or vertical line. Increments if horizontal side is hit.

'''

#=== Function Definitions ===#

def cuttingSeq(input_slope, iter, sequence, comp_x = 1, comp_y = 1):
	
	if iter <= 0:
		return sequence
	
	comp_slope = (comp_y * 1.0)/ comp_x
# 	print comp_slope

	if input_slope > comp_slope:
# 		print "A"
		sequence = sequence + "A"
		return cuttingSeq(input_slope, iter - 1, sequence, comp_x, comp_y + 1);
	
	elif input_slope < comp_slope:
# 		print "B"
		sequence = sequence + "B"
		return cuttingSeq(input_slope, iter - 1, sequence, comp_x + 1, comp_y);
	else:
		return sequence