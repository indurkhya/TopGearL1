# Using loop structures print even numbers between 1 to 100.
# a) By using For loop, use continue/ break/ pass statement to skip odd numbers.
#     i) Break the loop if the value is 50
#     ii) Use continue for the values 10,20,30,40,50
# b) By using while loop, use continue/ break/ pass statement to skip odd numbers.
#       i) Break the loop if the value is 90
#       ii) Use continue for the values 60,70,80,90

#
# for i in range(1,101):
#     if i%2!=0:
#         print("Odd number: ",i)
#     else:
#         print("Even number: ",i)
#
# for i in range(1,100):
#     #  using pass keyword but it will not do anything as in python pass means nothings
#     if i%10!=0:
#         pass
#     if i%10==0:
#         print(i)
#     #     i) Break the loop if the value is 50
#         if i == 50:
#             break
#     #     ii) Use continue for the values 10,20,30,40,50
#     continue

i =1
# while i<101:
#     if i%2!=0:
#         print("Odd number: ",i)
#     else:
#         print("Even number: ",i)
#     i +=1

while i<101:
    if i <60:
        pass
    elif i == 100:
        continue
    elif i%10==0:
        print(i)
        if i ==90:
            break
    i += 1