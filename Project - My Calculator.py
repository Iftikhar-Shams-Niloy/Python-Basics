#Try and Except:
#Building a Calculator:
print("\n$$$[[[Python calculator by NiloY]]]$$$\n")
print("How to use op/operands:")
print("1. to add, use + ")
print("2. to ditract, use -")
print("3. to devide, use /")
print("4. to multiply, use x")
print("5. to exponent(to the power), use ^")
print()
while(1):
    try:
        num1 = float(input("Enter first number:"))
        op = input("Enter operator/exponent:")
        num2 = float(input("Enter second number:"))

        if op == "+":
            print("Result :",num1 + num2)
        elif op == "-":
            print("Result :",num1 - num2)
        elif op == "x":
            print("Result :",num1 * num2)
        elif op == "/":
            print("Result :",num1 / num2)
        elif op == "^":
            print("Result :",num1**num2)
        else:
            print("### Invalid Operator!!! ###")

    except ValueError:
        print ("### Invalid Input!!! ###")
    except ZeroDivisionError:
        print("### Math Error (-_-) ###")
    print("---------------------------")
