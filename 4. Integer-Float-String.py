#Float, Integer and String:

#INTEGER :
print("\n>>>INTEGER :")
num1 = 20
print(type(num1))
print(num1)

#FLOAT / FLOATING POINT:
print("\n>>>FLOAT")
num2 = 20.24
print(type(num2))
print(num2)

#STRING:
print("\n>>>STRING:")
name1 = "Python"
print(type(name1))
print(name1)
name2 = "420.69"
print(type(name2))
print(name2)

#CONVERSION:
print("\n>>>CONVERSION")
num3 = int(num2) # num2 was a floating point number (before conversion)
print(type(num3))  # now it is converted to integer, which is assigned in num3
print(num3)

num4 = int(420.69) # num4 was supposed to be a floating point number (before conversion)
print(type(num4)) # now it is converted to integer, which is assigned in num4
print(num4)

num5 = float(num1)  # num1 was an integer/decimal number (before conversion)
print(type(num5)) # now it is converted to float, which is assigned in num5
print(num5)

making_string = str(num2) # num2 was a floating point number (before conversion)
print(type(making_string)) # now it is converted to string, which is assigned in making_string
print(making_string)

