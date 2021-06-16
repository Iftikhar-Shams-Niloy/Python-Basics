#Normal print
print("Hello World,")
print("Hello Everyone.")

#Entering a new line using "\n"
print("Hello \nWorld")
print("\nHello \nEveryone.")

#Using end='' to not to go to the next line after one print()
print("Helllo World, ", end='')
print("Hello Everyone")

#Using sep='' to seperate objects
print(1,2,3,4,5)
print(1,2,3,4,5,sep=' * ')

#We can also use sep='' and end='' together
print(1,2,3,4,5,sep=' * ',end='#')

#Printing variables(String)
name = ("Niloy")
print(name)
print("My name is "+ name)
print("My name is {}".format(name))

#Printing an integer and string in the same line:
name = ("Niloy")
age = 20
print("My name is "+name+". I am "+str(age)+" years old.")
print("My name is {}. I am {} years old.".format(name,age))

#Pringting a number in a sentence
age = 20
print('''\nSo you are %d years old. You don't look like %d.
You look younger than %d'''%(age, age,age))

#Printing/writinga paragraph
print('''
Hello everyone, My name is Niloy.
I am a student in BRACU.
I love programming.
So, that's why I choosed CSE as my major.
''')

#Directly printing out the answer of a math
num = 10
print(num+num) #addition
print(num-num) #subtraction
print(num*num) #multiplication
print(num/num) #division
print(num**num)#exponent
