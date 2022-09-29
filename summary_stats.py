#!/usr/bin/python3
"""
Reads a list of numbers from file or STDIN and prints
* number of items
* mean
* media
* mode
* standard deviation

usage:
	summary-stats.py [file]

	If no file is given, read from STDIN
"""

import sys
import re

def input_nums(fh):
	"""
	Reads numeric text data from given file object and
	returns a list of integers
	"""
	nums = []
	non_digits = r'\D+'
	for line in fh:
		# extract digits (numeric text data) and convert to list of floats
		n = [float(e) for e in re.split(non_digits, line) if e]
		if n:
			nums.extend(n)
	return nums

def mean(nums):
	"""
	Returns the arithmetic mean (average) as a floate,
	of a given list of floats
	"""
	# TODO
	return None

def median(nums):
	"""
	Returns the median as a float of a given list of floats
	"""
	# TODO
	return None

def mode(nums):
	"""
	Returns the mode as a float of a given list of floats
	"""
	# TODO
	return None

def variance(nums):
	"""
	Returns the sample variance as a float of a given list of floats
	"""
	# TODO
	return None

def std_dev(nums):
	"""
	Returns the sample standard deviation as a float of a given list of floats
	"""
	# TODO
	return None

if __name__ == '__main__':
	# file name is given as first argument, or use STDIN
	fh = sys.stdin
	if len(sys.argv) > 1:
		if len(sys.argv) == 2:
			fname = sys.argv[1]
			fh = open(fname, 'r')

	nums = input_nums(fh)
	print(nums)
	fh.close()
