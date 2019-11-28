# Write a program to read string and print each character separately.

#     a) Slice the string using slice operator [:] slice the portion the strings to create a sub strings.

# st = "Welcome to the world of Python"
st = input("Enter the string here: ")
start = int(input("Enter the Starting Slice value: "))
# Note always give one chracter extra as the end point of string bcz it will print n-1 characters.
end = int(input("Enter the Slice value here till which character you want to sub string the main string: "))
print("Sub string is:", st[start:end])

#     b) Repeat the string 100 times using repeat operator *

rt = "Welcome to the world of Python \n "
rt_string = rt*10
print("String is repeated 100 time of main string:\n",rt_string)

#     c) Read string 2 and concatenate with other string using + operator.

r1 = "Welcome to the world of Programming "
r2 = "Welcome to the world of Python"

concat = r1+ r2
print(concat)
