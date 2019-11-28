# Write a program to receive 5 command line arguments and print each argument separately.
# Example: >> python test.py arg1 arg2 arg3 arg4 arg5
# a) From the above statement your program should receive arguments and print them each of them.
import sys
#
print("The Number of arguments passed is: ",len(sys.argv))
print(sys.argv[1:])


# b) Find the biggest of three numbers, where three numbers are passed as command line arguments.
#
print("The Number of arguments passed is: ",len(sys.argv))
print(sys.argv[1:])
print(max(sys.argv[1:]))

