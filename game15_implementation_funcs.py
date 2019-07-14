from decorators import clear_terminal_before_func
from supporting_funcs import create_2d_array


@clear_terminal_before_func
def greet_user():

	from os import uname

	print("""Hello {}! Welcome to the game of 15.
	The game consists of ....""".format(uname()[1]))
	return None


def initialise_board(dim):
	# initialise 2d array, ascending order. create_2D_array() uses itertools.counter() method.
	board_asc = create_2d_array(dim=dim, beg=0, step=1)

	# Sort descending the 2D array. sorted() returns a copy of the iterable passed, board_asc is unmuted.
	board_desc = sorted([sorted(sub_list, reverse=True) for sub_list in board_asc],
	                    reverse=True)
	# As per specs, if dimensions is even, swap positions of tiles 1 and 2.
	if dim % 2 == 0:
		# swap_tiles() returns a copy of the board_desc.
		return swap_tiles(array=board_desc, a_row=dim - 1, a_col=dim - 2, b_row=dim - 1, b_col=dim - 3)
	else:
		return board_desc


def output_board_row(row):
	return map(lambda x: (x == 0 and " [_] ") or
	                     (x >= 10 and "[{}] ".format(x)) or
	                     (" [{}] ".format(x)),
	           row)


def draw_board(state):
	for row in state["board"]:
		print("".join(output_board_row(row)))  # print() will automatically print "\n" at the end of each row.
	return None


def get_tile(tile, dim):
	return (tile.isdigit()  # check the tile is a number
	        and (int(tile) in range(1, dim * dim))  # check the tile is in the board.
	        and (int(tile))  # return the tile as an int.
	        or get_tile(input("Invalid input. Try again!\nPlease enter the tile you want to move: "),
	                    dim=dim))  # or prompt again.


def is_legal_move(board, row, col):
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
	for row in range(len(array)):
		for col in range(len(array)):
			if element == array[row][col]:
				return (row, col)
	# else raise error
	raise ValueError("Something's wrong with either the the board or the tile values. Check the 🐛")


def swap_tiles(array, a_row, a_col, b_row, b_col):
	from copy import deepcopy
	arr = deepcopy(array)
	arr[a_row][a_col], arr[b_row][b_col] = arr[b_row][b_col], arr[a_row][a_col]
	return arr


def play(state):
	draw_board(state)
	if state["board"] != state["winning_board"]:  # check user hasn't won.
		play(run_step_of_the_game(state))
	else:
		exit("ftw! You won! Now go get some cookies :D")  # positive reinforcement!


def run_step_of_the_game(state):
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
		print("You chose a tile which does not seem to be movable, please choose anew.")
		return state
