#!/usr/bin/python3

##############
# decorators #
##############


def clear_terminal_before_func(func):
	"""
	func to decorate another func which prints to terminal, but first clears it.
	:param func: function with output on user's terminal.
	:return: wrapper_clear_terminal(*args, **kargs)
	"""
	from os import (system, name)
	from time import sleep
	from functools import wraps

	@wraps(func)
	def wrapper_clear_terminal(*args, **kargs):
		system('cls' if name == 'nt' else 'clear')
		sleep(1)
		return func(*args, **kargs)
	return wrapper_clear_terminal
