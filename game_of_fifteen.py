#!/usr/bin/python3

#########
# specs #
#########

# tl;dr
# Implement the Game of Fifteen, per the below.
# $ python game_of_fifteen.py 3
# WELCOME TO GAME OF FIFTEEN
#
# 8  7  6
#
# 5  4  3
#
# 2  1  _
#
# Tile to move:

# Full specs: https://docs.cs50.net/problems/fifteen/fifteen.html
# OOP solution from CS50 staff: https://www.youtube.com/watch?v=XAisU3eJ9Nw
# My own old solution in C: https://gist.github.com/gsime1/30e2e2a3dc6f2b216f955626182288c9

from sys import (argv, exit)
from supporting_funcs import (is_legal_argv, create_2d_array, assoc)
from game15_implementation_funcs import (greet_user, play, initialise_board)


DIM_MIN = 3
DIM_MAX = 9


def main():

	global DIM
	if not is_legal_argv(arg_vec=argv, desired_len=2, arg_to_check=1, within_range=[DIM_MIN, DIM_MAX]):
		exit("Usage: python fifteen.py D.\nThe desired dimension (D) must be a number between {} and {}.".
		     format(DIM_MIN, DIM_MAX))
	else:
		DIM = int(argv[1])

	greet_user()

	# and play! Recursively until user wins. State dictionary updates params of the game each step.
	play({"dimension": DIM,
	      "board": initialise_board(dim=DIM),  # create initial board as per specs.
	      "winning_board": assoc(array=create_2d_array(dim=DIM, beg=1, step=1),  # winning board is ascending 2D array
	                             row=DIM-1,  # last row
	                             col=DIM-1,  # last col
	                             value=0),   # winning board has 0 as last element of 2D array.
	      "tile": None,  # the first tile to move is None as user will only input after first play() call.
	      "blank_tile_row": DIM-1,   # position of blank tile at the beginning.
	      "blank_tile_col": DIM-1})  # position of blank tile at the beginning.


if __name__ == "__main__":
	main()


#########
# Notes #
#########
#        -1- Why do we use global to create the DIM constant?
#        -2- How does the play() function work?
#        -3- What is assoc()?
#        -4- Why are some imports within function def scopes?
#        -5- What could be improved?
#
