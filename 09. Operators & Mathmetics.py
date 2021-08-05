#Maths in python

    #Additions :
print("### ADDITION ###")
n1 = 12
n2 = 13
addition = n1 + n2
addition1 = n1 + 25
print("Addition(1) :",addition)
print("Addition(2) :",addition1) #Add 2 numbers directly
addition2 = n1+n1+n2+n2
print("Addition(3) :",addition2)

    #Substractions :
print("\n ### SUBSTRACTION ###")
n1 = 10
n2 = 4
sub1 = n1 - n2
sub2 = n2 - n1
add_sub = (n1+n1)-(n2+n2)
print("Substraction(1) :",sub1)
print("Substraction(2) :",sub2)
print("Addition & Substraction:",add_sub)

    #Multiplicatoins :
print("\n ### MULTIPLICATION ###")
n1 = 5
n2 = 3
multi1 = n1*n2
multi2 = n1*5
multi3 = n1*5+n1-n2
print("Multiplication(1) :",multi1)
print("Multiplication(2) :",multi2)
print("Multiplication(3) :",multi3)

    #Divisions :
print("\n ### DIVISION ###")
n1 = 15
n2 = 3
div1 = n1 / n2
div2 = n1 / 2
floor_div = n1 // 2
print("Division(1) :",div1)
print("Division(2) :",div2)
print("Division(3) :",floor_div)

    #Modulus :
print('\n ### MODULUS ###')
n1 = 15
print("Modulus :", n1%2)
print("Modulus :", n1%6)
print("Modulus :", n1%3)

    #Exponent :
print('\n ### EXPONENT ###')
num = 2
print("Exponent(1) :",2**2)
print("Exponent(2) :",2**3)
print("Exponent(3) :",2**4)

    #Using Constants of the 'math' module
import math
print("\n ### USING CONSTANTS ###")
pi = math.pi
print("The value of pi :",pi)
tau = math.tau
print("The value of tau :",tau)
euler_num = math.e
print("The Euler's number :",euler_num)
rad = 5
circle = 2*(math.pi)*(rad**2)
print("When radius = 5, Area =",circle)
infinity = math.inf #We can also use infinity in python maths

    #Factorial :
print("\n ### FACTORIAL ###")
num = 10
factorial = 1
for i in range(num):
    factorial *= (i+1)
print("Factorial of 10(1) :",factorial)
# Alternate method:
print("Factorial of 10(2) :",math.factorial(num))

    #Ceiling and Floor value :
print("\n ### CEILING & FLOOR ###")
num = 125.69696969
num2 = -14.33425
print("Floor :",math.floor(num))
print("Ceil :",math.ceil(num))
print("Floor(Negative) :",math.floor(num2))
print("Ceil(Negative) :",math.ceil(num2))
