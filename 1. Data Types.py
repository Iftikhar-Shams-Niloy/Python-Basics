#DATA TYPES IN PYTHON:

# 1.Interger / int() :[Decimal point numbers]
print("\n***Integer***\n")
age = 20
print(type(age))
print(age)

# 2. Floating Point / float() :
print("\n***Floating Point***\n")
cgpa = 3.94
print(type(cgpa))
print(cgpa)

### Converting float to integer:
print("\n***Conversion From Float to Integer***\n")
cgpa = 3.75
cgpa = int(cgpa)
print(type(cgpa))
print(cgpa)

# 3. Stings str()
print("\n***Strings***\n")
name = "Niloy"
age = str(20) #It makes 20 (Which is an integer
print(type(name))
print(type(age))
print(name + age)
print(name + " is " + age + " old.")

# 4. Lists - list - ["name1", "name2", 100]
print("\n***Lists***\n")
name_list = ["Niloy", "Ismail", "Khaled", "Rahat"]
num_list = [1,2,3,4,5]
name_num_list = ["Niloy",21,200,"Shams"]
print(type(name_list))
print(type(num_list))
print(name_list)
print(num_list)
print(name_num_list)

# 5. Dictionaries - dict - {"key" : "Value"}
print("\n***Dictionaries***\n")
price = {"Apple": 100 , "Orange" : 120, "Dragon Fruit" : 1000}
print(type(price))
print(price["Apple"])
print(price["Dragon Fruit"])

# 6. Tuples - tup - ("Object1","Object2, 69)
print("\n***Tuples***\n")
student_name = ("Niloy", "Toha", "Proma" ,1 , 2,155)
#Tuples are lists that are immutable
print(type(student_name))
print(student_name)

# 7. Sets - set - {"Obj1","Obj2","Obj3"}
print("\n***Sets***\n")
obj_set = {"a","b","c",1,2,3}
print(type(obj_set))
print(obj_set)

# 8. Booleans - bool - Logical value indicating True and False
print("\n***Booleans***\n")
exam_pass = True
in_relationship = False
print(type(exam_pass))
print(type(in_relationship))
print(exam_pass)
print(in_relationship)
