# Create a list with at least 10 elements having integer values in it;

#        Print all elements
tup = (75,25,85,45,85,96,85,85,74,70)

for i in range(0,len(tup)):
    print(tup[i])

#        Perform slicing operations
print("Slicing the List till 4th character: ",tup[0:5])

#        Perform repetition with * operator
print("Repeating the List for 5 times: ",tup*2)

#        Perform concatenation with other list.

t1 = (1,25,48,52,75)
t2 = (45,28,65,35,85)
print("Concatenating the list: ",t1+t2)
