#!/usr/bin/python3

#########
# specs #
#########
#  Write a program that prints out the numbers 1 to 100 (inclusive). 
#  If number is divisible by 3, print Crackle.
#  If it's divisible by 5, print Pop.
#  If it's divisible by both 3 and 5, print CracklePop. 
#  Use any language.


# main
def main():

	# Use short-circuiting to abstract imperative conditional logic in a lambda expression.
	# In Python, expression results are always printed to the console.
	cracklepop = lambda number: (((number % 3 == 0 and number % 5 == 0) and "CracklePop")
	                                  or ((number % 3 == 0) and "Crackle")
	                                  or ((number % 5 == 0) and "Pop")
	                                  or number)

	# save results in a list (we might need it in some other versions of this programme).
	results = [cracklepop(num) for num in range(1, 101)]

	# print results.
	for result in results:
		print(result)


if __name__ == "__main__":
	main()


############
# Learning #
############
#        -1- Why don't we use print("Crackle") in the short-circuited expressions?
#            Because then the rightmost element of the expressions would return None which, being falsy,
#            would mess up our conditions.
#
#            For instance, if we passed as argument 10, the conditions would be evaluated as follows
#            1st expression: (10 % 3 == 0 and 10 % 5 == 0) and print(10) -> False(!) and True and None+sideEffect
#            2nd expression: (10 % 3 == 0) and and print(10) -> False(!) and None+sideEffect
#            3rd expression: (10 % 5 == 0) and and print(10) -> True and None+sideEffect
#            4th expression: print(10) -> None+sideEffect
#
#            1st and 2nd expressions would stop at the (!), 3rd and 4th expressions would print to console.

#            >>> cracklepop(10)
#            >>> Pop
#            10
#
#        -2- Possible improvements?
#            The most obvious improvement would be to have the user decide the range, now hard-coded [1, 101)
#            This could be done by prompting the user the range as a command line argument to the python interpreter.
