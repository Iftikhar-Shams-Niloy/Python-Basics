#Normal print
print()
print(">>> 1.NORMAL PRINT :")
print("Hello World,")
print("Hello Everyone.")

#Entering a new line using "\n"
print()
print(">>> 2.NEW LINE :")
print("Hello \nWorld")
print("\nHello \nEveryone.")

#Using end='' to not to go to the next line after one print()
print()
print(">>> 3. USING end='' :")
print("Helllo World, ", end='')
print("Hello Everyone.")

#Using sep='' to seperate objects
print()
print(">>> 4. USING sep='' :")
print(1,2,3,4,5)
print(1,2,3,4,5,sep=' * ')

#We can also use sep='' and end='' together
print()
print(">>> 5. USING sep='' and end='' together :")
print(1,2,3,4,5,sep=' * ',end='#')

#Printing variables(String)
print()
print(">>> 6. PRINTING VARIABLES :")
name = ("Niloy")
print(name)
print("My name is "+ name)
print("My name is {}".format(name))

#Printing an integer and string in the same line:
print()
print(">>> 7. PRINTING DIFFERENT TYPES OF VARIABLES TOGETHER :")
name = ("Niloy")
age = 20
print("My name is "+name+". I am "+str(age)+" years old.")
print("My name is {}. I am {} years old.".format(name,age))

#Printing numbers in a sentence
print()
print(">>> 8. PRINTING NUMBERS WITH STRING :")
age = 20
print('''So you are %d years old. You don't look like %d.
You look younger than %d'''%(age, age,age))

gpa = 4.97
print("Your GPA is %f"%(gpa))
pi = 3.1416
print("The value of pi is : %.2f"%(pi))

#Printing variables (any data-type):
print()
print(">>> 9. PRINTING VARIABLES (ANY DATA-TYPE) :")
print(f"I am {name}. I am {age} years old. My GPA is : {gpa}")

#Printing/writing a paragraph
print()
print(">>> 10. WRITING A PARAGRAPH :")
print('''
Hello everyone, My name is Niloy.
I am a student in BRACU.
I love programming.
So, that's why I choosed CSE as my major.
''')

#Directly printing out the answer of a math
print()
print(">>> 11. DIRECTLY PRINTING OUT THE ANSWER OF A MATH:")
num = 10
print("Addition :",num+num) #addition
print("Subtraction :",num-num) #subtraction
print("Multiplication :",num*num) #multiplication
print("Division :",num/num) #division
print("Exponent :",num**num)#exponent
