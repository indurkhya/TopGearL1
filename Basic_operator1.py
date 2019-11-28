# Write a program to find the biggest of 3 numbers (Use If Condition)

lis = [24,52,50]
print(max(lis))


# Write a program to find given number is odd or Even

num = int(input("Enter the number: "))

if num%2==0:
    print("Entered number is Even")
else:
    print("Entered number is Odd")


# Write a program to find the number is Prime or not.

number = int(input("Enter the number: "))
if number > 1:

    # Iterate from 2 to n // 2
    for i in range(2, number // 2):
        if (number % i) == 0:
            print(number, "is not a prime number")
            break
    else:
        print(number, "is a prime number")

else:
    print(number, "is not a prime number")



