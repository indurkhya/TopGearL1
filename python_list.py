# Write a program to create two list A & B such that List A contains Employee Id, List B contain Employee name
# (minimum 10 entries in each list) & perform following operation
#      a) Print all names on to screen
#      b) Read the index from the  user and print the corresponding name from both list.
#      c) Print the names from 4th position to 9th position
#      d) Print all names from 3rd position till end of the list
#      e) Repeat list elements by specified number of times (N- times, where N is entered by user)
#      f)  Concatenate two lists and print the output.
#      g) Print element of list A and B side by side.(i.e. List-A First element, List-B First element )

lisName = []
lisEmp = []

for i in range(4):
    num = int(input("Enter Employee ID: "))
    lisName.append(num)
    num1 = input("Enter Employee Name: ")
    lisEmp.append(num1)

# print(lisName)
# print(lisEmp)

# a) Print all names on to screen
for item in lisEmp:
    print(item, end=" ")
print("\n")

# b) Read the index from the  user and print the corresponding name from both list.

indx = int(input("Enter the index: "))
if lisName[indx] in lisName:
    print("The Employee ID is: ", lisName[indx])
if lisEmp[indx] in lisEmp:
    print("The name is: ", lisEmp[indx])

# c) Print the names from 4th position to 9th position
print(lisEmp[4:9])
print(lisName[4:9])

# d) Print all names from 3rd position till end of the list
print(lisName[3:])

#  e) Repeat list elements by specified number of times (N- times, where N is entered by user)
n = int(input("Enter the number for repeating the list: "))
op = lisName*n
op1 = lisEmp*n
print(op)
print(op1)

#  f)  Concatenate two lists and print the output.
cancat = lisEmp + lisName
print(cancat)

#  g) Print element of list A and B side by side.(i.e. List-A First element, List-B First element )

for i in range(4):
    print(lisName[i],":",lisEmp[i])
# ####################################################################################################################
