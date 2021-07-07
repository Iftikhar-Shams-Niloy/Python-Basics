n = int(input("How many numbers? : "))
max = 0
min = 0
total = 0
for i in range(n):
    num = int(input("Enter {}no. number :".format(i+1)))
    if  num>= max or num == max:
        max = num
    else:
        max = max
    if num <= min or min == 0:
        min = num
    else:
        min = min
    total = total+num
#print("Maximum : {}".format(max))
print("Maximum : {}".format(max))
print("Minimum : {}".format(min))
print("Total : {}".format(total))
print("Average is {}".format(total/n))