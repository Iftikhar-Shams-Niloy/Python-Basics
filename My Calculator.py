#Try and Except:
#Building a Calculator:
print("$$$[[[Python calculator by NiloY]]]$$$")
print()
print("How to use op/operands:")
print("1. to add, use + ")
print("2. to ditract, use -")
print("3. to devide, use /")
print("4. to multiply, use *")
print("5. to exponent(power), use **")
print()
while(1):
    try:
        num1 = float(input("Enter first number:"))
        op = input("Enter operator/exponent:")
        num2 = float(input("Enter second number"))

        if op == "+":
            print(num1 + num2)
        elif op == "-":
            print(num1 - num2)
        elif op == "*":
            print(num1 * num2)
        elif op == "/":
            print(num1 / num2)
        elif op == "**":
            print(num1**num2)
        else:
            print("Invalid Operator")

    except ValueError:
        print ("Invalid Input")
    except ZeroDivisionError:
        print("Math Error (-_-)")

