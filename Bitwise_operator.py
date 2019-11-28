# Read 2 numbers to variable a and b and perform all bitwise operations on that numbers.
# x << y
# Returns x with the bits shifted to the left by y places (and new bits on the right-hand-side are zeros). This is the same as multiplying x by 2**y.
# x >> y
# Returns x with the bits shifted to the right by y places. This is the same as //'ing x by 2**y.
# x & y
# Does a "bitwise and". Each bit of the output is 1 if the corresponding bit of x AND of y is 1, otherwise it's 0.
# x | y
# Does a "bitwise or". Each bit of the output is 0 if the corresponding bit of x AND of y is 0, otherwise it's 1.
# ~ x
# Returns the complement of x - the number you get by switching each 1 for a 0 and each 0 for a 1. This is the same as -x - 1.
# x ^ y
# Does a "bitwise exclusive or". Each bit of the output is the same as the corresponding bit in x if that bit in y is 0, and it's the complement of the bit in x if that bit in y is 1.


a = 80    # 10100   01011
b = 30    # 01010   10101
# AND operator
print(a & b)
# OR operator
print(a | b)
# XOR operator
print(a ^ b)
# NOT operator
print(~a)
# AND operator
print(~b)
c = ~a + ~b
print(c)
# operator
print(a << b)
# operator
print(a >> b)
