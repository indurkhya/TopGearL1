# Create a list of 5 names and check given name exist in the List.

#         a) Use membership operator (IN) to check the presence of an element.
#         b) Perform above task without using membership operator.
#         c) Print the elements of the list in reverse direction.

lis =[]
name1 =[]
for i in range(5):
    name = input("Enter the Name: ")
    lis.append(name)
    name1.append(name)

#         a) Use membership operator (IN) to check the presence of an element.

for i in range(5):
    if name not in lis:
        print("Entered name is not present")
    else:
        print("Entered name is present in the list ",lis[i])

#         b) Perform above task without using membership operator.

for i in range(5):
    if name1[i] != lis[i]:
        print("Entered name is not present")

    else:
        print("Entered name is present in the list ",lis[i])

#         c) Print the elements of the list in reverse direction.

# By Slice method
print(lis[::-1])
# By Reverse method
lis.reverse()
print(lis)
