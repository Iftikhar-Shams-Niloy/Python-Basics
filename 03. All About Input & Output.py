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
making_list = list(map(int,input("#CASE 3: Enter 3 numbers[Using coma(,)]: ").split(",")))#Here int decides the input type

#Enter numbers using coma(,) in between.... Then press enter
print("CASE 3:",making_list)
#We can also use 'tuple' nstead instead of 'list', with the inputs.

#Taking multiple input in a line (Case 4):
a, b, c = list(input("#CASE 4: Enter 3 Words[Using coma(,)]: ").split(","))#Enter 3 elements using coma(,) in between.... Then press enter
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
# Case 4:

name = input("Enter your name:")
age = int(input("Enter your age :"))
print("4_1. Your age is %d" %age)
print("4_2. Your name is %s"%name)
print("4_3. Your name is %s and you are %d years old"%(name,age))
# Case 5:
print(f"5. Your name is {name} and you are {age} years old")
# Case 6:
numb_float = float(input("Enter a floating point number:"))
print("6_1. Your number:%f"%numb_float)
print("6_2. Your number:%.2f"%numb_float)
