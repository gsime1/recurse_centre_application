def is_legal_argv(arg_vec, desired_len, arg_to_check, within_range):
	return ((len(arg_vec) == desired_len)
			and (arg_vec[arg_to_check].isdigit())
			and (int(arg_vec[arg_to_check]) in range(within_range[0], within_range[1]+1))  # rightmost range included
	        or False)


def create_2d_array(dim, beg, step):
	from itertools import count

	if all(map(lambda x: isinstance(x, int), [dim, beg, step])):
		counter = count(beg, step)
		return [list(next(counter) for _ in range(dim))
		        for _ in range(dim)]
	else:
		raise TypeError("All arguments provided must be of type int")


def assoc(array, row, col, value):
	from copy import deepcopy

	a = deepcopy(array)
	a[row][col] = value
	return a

