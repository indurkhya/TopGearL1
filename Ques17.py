# Write program to find the biggest and Smallest of N numbers.
#       PS: Use the functions to find biggest and smallest numbers.


def biggest(no):
    return max(no)


def smallest(no):
    return min(no)

lis =[]
n = int(input("Enter the Nth number: "))
for i in range(0,n):
    num = int(input("Enter List of Number: "))
    lis.append(num)

print(lis)
print("The Biggest Number in the List is: ",biggest(lis))
print("The smallest Number in the List is: ",smallest(lis))


