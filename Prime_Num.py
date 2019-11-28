# Write program to perform following:
#      i) Check whether given number is prime or not.
#     ii) Generate all the prime numbers between 1 to N where N is given number.

# 1 3 5 7 11 13 17 19

num = int(input("Enter the Number: "))
if num==1:
    print(f"{num} is a Prime Number")
elif num%2==0:
    print(f"{num} is not a Prime Number ")
else:
    print(f"{num} is a Prime Number")

#
if num > 1:
    for i in range(1,num):
        if i%2==0:
            print(f"{i} is not a prime number")
        else:
            print(f"{i} is a prime number")
else:
    print(f"{num} is not a prime number")


# If given number is greater than 1
# if num > 1:
#
#     # Iterate from 2 to n / 2
#     for i in range(2, num // 2):
#
#         # If num is divisible by any number between
#         # 2 and n / 2, it is not prime
#         if (num % i) == 0:
#             print(num, "is not a prime number")
#             # break
#     else:
#         print(num, "is a prime number")
#
# else:
#     print(num, "is not a prime number")
#



