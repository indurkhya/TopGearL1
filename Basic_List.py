# Create a list with at least 10 elements having integer values in it;

#        Print all elements
lis = [75,25,85,45,85,96,85,85,74,70]

for i in range(0,len(lis)):
    print(lis[i])

#        Perform slicing operations
print("Slicing the List till 4th character: ",lis[0:5])

#        Perform repetition with * operator
print("Repeating the List for 5 times: ",lis*2)

#        Perform concatenation with other list.

l1 = [1,25,48,52,75]
l2 = [45,28,65,35,85]
print("Concatenating the list: ",l1+l2)