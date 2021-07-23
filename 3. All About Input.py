# All of Input:

'''We use the input() function to
take input from the user. And then we
use print() function to show that value
on the screen'''
#Taking input (CASE 1):
x1 = input("# CASE 1: Enter Something:")
print("#CASE 1: "+x1)
#Defining an Input (CASE 2):
x2 = int(input("# CASE 2: Enter a number:"))
print("CASE 2:",x2)
#Taking inputs as list elements (Case 3):
making_list = list(map(int,input("#CASE 3: Enter 3 numbers(Using Space): ").split(" ")))#Here int decides the input type
print("CASE 3:",making_list)
#Taking multiple input in a line (Case 4):
a, b, c = list(input("#CASE 4: Enter 3 Words(Using Space): ").split(" "))#Enter 3 numbers using space in between.... Then press enter
print("CASE 4:{} {} {}".format(a,b,c))
#Taking multiplle input defining it! (Case 5):
x, y, z = list(map(int,input("#CASE 5: Enter 3 numbers(Using Space): ").split(" ")))
print("#CASE 5:",x,y,z)

### Ways of uisng Inputs! ###
print("\n### Ways of using Inputs! ###")
n = input("Enter you name :")
# Case 1 :
print("1. Your name is "+n)
# Case 2 :
print("2. Your name is {}".format(n))
# Case 3 :
print("3. Your name is",n)
# Case 4(In case of int or float only):
age = int(input("Enter your age :"))
print("4. Your age is %d" %age)
