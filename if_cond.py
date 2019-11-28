# Write a program to find the biggest of 4 numbers.
#    a) Read 4 numbers from user using Input statement.
#    b) extend the above program to find the biggest of 5 numbers.
# (PS: Use IF and IF & Else, If and ELIf, and Nested IF)


num1 = int(input("Enter first Number: "))
num2 = int(input("Enter first Number: "))
num3 = int(input("Enter first Number: "))
num4 = int(input("Enter first Number: "))

# Comparison the First number with rest three number
if (num1 >= num2) and (num1 >= num3) and (num1 >= num4):
    largest = num1
# Comparison the Second number with rest three number
elif (num2 >= num1) and (num2 >= num3) and (num2 >= num4):
    largest = num2

# Comparison the Third number with rest three number
elif (num3 >= num1) and (num3 >= num2) and (num3 >= num4):
    largest = num3
else:
    largest = num4

print("The Biggest number out of four input value is ",largest)
# print("The Biggest number from the",num1,",",num2,",",num3,",",num4,"is ",largest)

