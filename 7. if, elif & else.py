#if , elif(Else If) & else :

'''if/elif/else is used to make some blocks
of codes only when the text expression/condition
True...'''
# Using if,elif and else (Example1):
print("\n>>>Example 1 :")
num = int(input("Enter a Number:"))
if num > 0 :
    print("You have entered a positive number!!!")
elif num <0 :
    print("You have entered a negative number!!!")
else:
    print("You have entered 0 !!!")

# Using if,elif and else (Example 2):
print("\n>>> Example 2 : ")
a, b, c = list(map(int,input("Enter 3 values(for a,b,c) using space after each: ").split(" ")))
if a > b and a > c:
    print("a is greatest")
elif b > a and b > c:
    print("b is greatest")
elif b == a or b ==c :
    print("Two numbers are same.")
    if b==a and a==c:
        print("Three numbers are same.")
elif b == c and a != c:
    print("Two numbers are same.")
else:
    print("c is greatest")

# Using if,elif and else (Example 3):
print("\n>>> Example 3 :")
print()
name = input("Enter your name :")
vowel = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
# To know about list, please check my previous programs
if any(element in vowel for element in name):
    print("There is vowel in your name.")
else:
    print("There is no  vowel in your name.")

# Using Nested If and else(Example 4):
print("\n>>>Example 4:")
a = int(input("Enter a number:"))
if a > 0 :
    print("The number is positive!")
    if a > 10:
        print("The number is greater than 10!")
        if a > 100:
            print("The number is greater than 100!")
elif a <= 0 :
    print("The number is 0 or negative!")
    if a <-10 :
        print("The number is less than -10!")
        if a<-100:
            print("The number is less than -100!")

# Using Nested If,elif and else Statemets (Example 5):
print("\n>>>Example 5:")
name1 = ["Iftikhar" , 10748]
name2 = ["Niloy" , 5916]
name3 = ["Ismail", 10750]
ask1 = input("What do you want to know?(name or roll) :")
if ask1 == "name" :
    ask2 =int(input("Enter the roll of the student :"))
    if ask2 == 10748:
        print("Student name :",name1[0])
    elif ask2 == 5916:
        print("Student name :",name2[0])
    elif ask2 == 10750:
        print("Student name :",name3[0])
    else:
        print("### Student name not found!!! ###")
elif ask1 == "roll":
    ask3 = input("Enter the name of the student :")
    if ask3 == "Iftikhar" :
        print("Student roll :",name1[1])
    elif ask3 == "Niloy" :
        print("Student roll :",name2[1])
    elif ask3 == "Ismail" :
        print("Student roll :",name3[1])
    else:
        print("### Student name not found!!! ###")
else:
    print("### Invalid Input!!! ###")