# Read 10 numbers from user and find the average of all.
# a) Use comparison operator to check how many numbers are less than average and print them
# b) Check how many numbers are more than average.
# c) How many are equal to average.

#
lis = []
# avg = 0
sum = 0
for i in range(10):
    num = input("Enter Number: ")
    lis.append(num)
    sum += int(lis[i])
    avg = sum/len(lis)
print(avg)
for i in range(10):
    if int(lis[i]) > avg:
        print("User number is greater than Avg value ",lis[i])
    elif int(lis[i]) < avg:
        print("User number is less than Avg value ",lis[i])
    else:
        print("Both Average value and the user number is same")