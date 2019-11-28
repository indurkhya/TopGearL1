# Write a program to generate a Fibonacci series of numbers.
# Starting numbers are 0 and 1,  new number in the series is generated by adding previous two numbers in the series.
# Example : 0, 1, 1, 2, 3, 5, 8,13,21,.....
#    a) Number of elements printed in the series should be N numbers, Where N is any +ve integer.
#    b) Generate the series until the element in the series is less than Max number.


def fibonacci(n):
    if n ==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

fibo= fibonacci(5)
# print(fibo)

value = int(input("Enter Nth Number : "))
if value < 0:
    print("Positive number is required")
else:
    print("fibonacci series: ",end=" ")
    for i in range(value):
        print(fibonacci(i),end=" ")