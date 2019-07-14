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
	# In Python, expression results are always printed to the console. monadic_print() will be used
	# as the right-most expression element, which will be evaluated if all expressions to its left evaluate to True.
	CracklePop_print = lambda number: ((number % 3 == 0 and number % 5 == 0) and (monadic_print("CracklePop")))\
	                                  or ((number % 3 == 0) and (monadic_print("Crackle")))\
	                                  or ((number % 5 == 0) and (monadic_print("Pop")))\
	                                  or (monadic_print(number))

	# save results in a list (we might need it in some other versions of this programme).
	results = [CracklePop_print(num) for num in range(1, 101)]

	# print results.
	for result in results:
		print(result)


# supporting_funcs.py functions
def monadic_print(string):
	"""
	monadic func returning its own argument.
	:arg string: string to be returned
	:return: string
	"""
	return string


if __name__ == "__main__":
	main()


#########
# Notes #
#########
#        -1- What would happen if we used the built-in print() instead of monadic_print()? 
#            The rightmost element of the expressions would return None (print built-in returns None)  
#            In the above example, 1st expression: (5 % 3 == 0 and 5 % 5 == 0) and None evaluates to False.
#                                  2nd expression: (5 % 3 == 0) and None evaluates to False.
#                                  3rd expression: (5 % 5 == 0) and None evaluates to True => print("pop").
#                                  4th expression: print(5) => side-effect function printing 5 to console. 
#            >>> CracklePop_print(5)
#            >>> Pop
#            5
#
#        -2- Why use monadic_print if we then still need to use built-in print to display the results?
#            The main advantage is the ability to reuse the CracklePop_print() function in other programmes
#            without having to embed the imperative logic to another programme we might be writing in the future. 
#        
#        -3- Possible improvements?
#            The most obvious improvement would be to have the user decide the range, now hard-coded [1, 101)
#            This could be done by prompting the user the range as a command line argument to the python interpreter.
