# Using loop structures print numbers from 1 to 100.  and using the same loop print numbers from 100 to 1 (reverse printing)
# a) By using For loop
# b) By using while loop
# c) Let mystring ="Hello world"
# print each character of mystring in to separate line using appropriate loop structure.

# a) By using For loop

for i in range(1,101):
    print(i)
    if i ==100:
        print("\n")
        for i in range(100,0,-1):
            print(i)


# b) By using while loop

i = 1
while i>=1:
    print(i)
    i = i+1
    if i ==101:
        while i>=1:
            if i ==101:
                print("\n")
                i -=1
            print(i)
            i -= 1


# print each character of mystring in to separate line using appropriate loop structure.

mystring ="Hello World"

for item in range(0,len(mystring)):
    print(mystring[item])