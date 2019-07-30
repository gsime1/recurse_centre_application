#!/usr/bin/python3

##################
# implementation #
#     funcs      #
##################

from decorators import clear_terminal_before_func
from supporting_funcs import create_2d_array


@clear_terminal_before_func
def greet_user():
	"""
	func greeting user and giving instructions. Decorated to clear the terminal before executing.
	:return: None, side-effect func.
	"""
	from os import uname

	return print("""Hello {} from the Recurse Centre!\n
	WELCOME TO THE GAME OF FIFTEEN\n
	The game is very simple, you just have to choose the tile you want to swap with the empty tile [_] and keep moving 
	them until the board, which is now upside down, starts again with [1] [2] [3] ... and ends with the empty tile [_].\n
	Can you do it?\n 
	Try! The board is here below, choose your first move!\n\n""".format(uname()[1]))


def initialise_board(dim):
	"""
	func to initialise the board as per specs. First creates ascending 2D array then uses sorted() and
	list comprehension to invert order.
	:param dim: dimension of the 2D array.
	:return: if dim is even the board with tiles [1] and  [2] swapped, else normal board.
	"""
	# initialise 2d array, ascending order. create_2D_array() uses itertools.counter() method.
	board_asc = create_2d_array(dim=dim, beg=0, step=1)

	# Sort descending the 2D array. sorted() returns a copy of the iterable passed, board_asc does not mutate.
	board_desc = sorted([sorted(sub_list, reverse=True) for sub_list in board_asc],
	                    reverse=True)
	# As per specs, if dim is even, swap positions of tiles [1] and [2].
	if dim % 2 == 0:
		# swap_tiles() returns a copy of board_desc.
		return swap_tiles(array=board_desc, a_row=dim - 1, a_col=dim - 2, b_row=dim - 1, b_col=dim - 3)
	else:
		return board_desc


def output_board_row(row):
	"""
	func to print the row of the board (list of ints) applying the right spacing to ensure tiles are aligned.
	Uses map() to apply a short-circuited lambda expression on each element of the list of int.
	:param row: list of integer contained in the outer list of the 2D array.
	:return: generator, will be actualised by "".join method in draw_board() func.
	"""
	return map(lambda x: (x == 0 and " [_] ") or
	                     (x >= 10 and "[{}] ".format(x)) or
	                     (" [{}] ".format(x)),
	           row)


def draw_board(state):
	"""
	func to draw the board for the game.
	:param state: dictionary containing the state variable of the game. state["board"] will be the returned 2D array
	              from initialise_board(dim).
	:return: None, side-effect func.
	"""
	for row in state["board"]:
		print("".join(output_board_row(row)))  # print() will automatically print "\n" at the end of each row.
	return None


def get_tile(tile, dim):
	"""
	func which recursively prompts the user for the tile they want to move.
	:param tile: string tile inputted by the user when prompted by the run_step_of_the_game() func.
	:param dim: dimension of the board, used to check tile is within board dimensions.
	:return: short-circuited expression checking tile is digit, within range and either returning the tile
	         as an int or recursively prompting the user after printing error message.
	"""
	return (tile.isdigit()  # check the tile is a number
	        and (int(tile) in range(1, dim * dim))  # check the tile is in the board.
	        and (int(tile))  # return the tile as an int.
	        or get_tile(input("Invalid input. Try again!\nPlease enter the tile you want to move: "),
	                    dim=dim))  # or prompt again.


def is_legal_move(board, row, col):
	"""
	func that checks if a tile at position board[row][col] is movable.
	:param board: 2D array updated and returned by the run_step_of_the_game() func.
	:param row: int returned by the linear_search() function.
	:param col: int returned by the linear_search() function.
	:return: bool value depending on the conditional expression evaluation.
	"""
	# get dim
	dim = len(board)

	# check if empty above the tile
	if (row > 0 and board[row - 1][col] == 0):
		return True
	# below the tile
	elif (row < dim - 1 and board[row + 1][col] == 0):
		return True
	# left-hand side of the tile
	elif (col > 0 and board[row][col - 1] == 0):
		return True
	# right-hand side of the tile
	elif (col < dim - 1 and board[row][col + 1] == 0):
		return True
	# illegal move
	else:
		return False


def linear_search(array, element):
	"""
	func to search though a 2D array, linear search algorithm.
	:param array: 2D array updated and returned by the run_step_of_the_game() func.
	:param element: int, tile the user provided to get_tile(input(...)) in the run_step_of_the_game() func.
	:return: tuple containing the indices of the element found, or error raised.
	"""
	for row in range(len(array)):
		for col in range(len(array)):
			if element == array[row][col]:
				return (row, col)
	# else raise error
	raise ValueError("Something's wrong with either the the board or the tile values. Check the 🐛")


def swap_tiles(array, a_row, a_col, b_row, b_col):
	"""
	func to swap two elements in a 2D array, uses deepcopy and returns a new object.
	:param array: 2D array updated with latest moves by the run_step_of_the_game() func.
	:param a_row: row index of element a to be swapped.
	:param a_col: col index of element a to be swapped.
	:param b_row: row index of element b to be swapped.
	:param b_col: col index of element b to be swapped.
	:return: deepcopy of initial 2D array with elements swapped.
	"""
	from copy import deepcopy
	arr = deepcopy(array)
	arr[a_row][a_col], arr[b_row][b_col] = arr[b_row][b_col], arr[a_row][a_col]
	return arr


def play(state):
	"""
	func that recursively play until game is won. Func recurses over run_step_of_the_game(), which applies
	the mutation necessary to the state dictionary for the next step in the game.
	:param state: dictionary containing the state variable of the game.
	:return: None or exit if game won.
	"""
	draw_board(state)
	if state["board"] != state["winning_board"]:  # check user hasn't won.
		play(run_step_of_the_game(state))
	else:
		exit("ftw! You won! Now go get some cookies :D")  # positive reinforcement!


def run_step_of_the_game(state):
	"""
	func where the actual steps of the game are implemented. Asks for the tile to move, looks for it and, if move is legal
	swaps tiles and updates position of blank tile.
	:param state: dictionary containing the state variable of the game.
	:return: the state dictionary, either successfully muted (if tile supplied by user was legal) or same state as the
	one provided as parameter.
	"""
	# ask the use which tile they want to move and update state["tile"] accordingly.
	state["tile"] = get_tile(input("Please enter the tile you want to move: "),
	                         dim=state["dimension"])

	# look for the tile the use wants to move
	row, col = linear_search(array=state["board"], element=state["tile"])

	# is_legal_move
	if is_legal_move(board=state["board"], row=row, col=col):

		# swap tiles and update state["board"]
		state["board"] = swap_tiles(array=state["board"],
		                            a_row=row,
		                            a_col=col,
		                            b_row=state["blank_tile_row"],
		                            b_col=state["blank_tile_col"])
		# we swapped the tile and the empty tile, so we update empty tile position
		state["blank_tile_row"] = row
		state["blank_tile_col"] = col

		return state

	else:
		print("You chose a tile which does not seem to be movable, please choose again.")
		return state
