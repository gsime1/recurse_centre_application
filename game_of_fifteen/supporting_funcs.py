#!/usr/bin/python3

###############
# generalised #
#   funcs     #
###############


def is_legal_argv(arg_vec, desired_len, arg_to_check, within_range):
	"""
	generalised func to check that argument vector of a program contains # elements and one of them is within a range.
	:param arg_vec: argv.
	:param desired_len: int, desired length to be checked.
	:param arg_to_check: int, index of the argument that needs to be within a certain range.
	:param within_range: list, list[0] lower range, list[1]+1 upper range.
	:return: short-circuited lambda expression, return bool.
	"""
	return ((len(arg_vec) == desired_len)
			and (arg_vec[arg_to_check].isdigit())
			and (int(arg_vec[arg_to_check]) in range(within_range[0], within_range[1]+1))  # rightmost range included
	        or False)


def create_2d_array(dim, beg, step):
	"""
	generalised func to create a 2D array given a certain dimension.
	:param dim: int, dimension of the 2D array.
	:param beg: int, first element of the array.
	:param step: int, increase of every consecutive element populating the array up to dim.
	:return: list of lists, 2D array.
	"""
	from itertools import count

	if all(map(lambda x: isinstance(x, int), [dim, beg, step])):  # checks all arguments are integers
		counter = count(beg, step)
		return [list(next(counter) for _ in range(dim))
		        for _ in range(dim)]
	else:
		raise TypeError("All arguments provided must be of type int.")


def assoc(array, row, col, value):
	"""
	generalised func to associate a new value to a 2D array.
	:param array: 2D array which will be deep copied and mutated.
	:param row: int index of the row of the element to be replaced with value.
	:param col: int index of the col of the element to be replaced with value.
	:param value: int, value to replace a[row][col] with.
	:return: copied array, muted.
	"""
	from copy import deepcopy

	a = deepcopy(array)
	a[row][col] = value
	return a

