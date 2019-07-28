def clear_terminal_before_func(func):
	from os import (system, name)
	from time import sleep
	from functools import wraps

	@wraps(func)
	def wrapper_clear_terminal(*args, **kargs):
		system('cls' if name == 'nt' else 'clear')
		sleep(1)
		return func(*args, **kargs)
	return wrapper_clear_terminal
