class student:
    def __init__(self, name,age,major,gpa,is_on_probation):
        self.name = name
        self.age = age
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation

CSE21101124 = student("Niloy", 21,"CSE",4.00 , False)
CSE21101125 = student("Sadi" , 20, "CSE", 3.78, False)
CSE21101126 = student("Shehab",21,3.98,"CSE", True )

st_name = int(input("Enter a roll: "))
if st_name == 21101124:
    print("Name      : " + CSE21101124.name)
    print("Age       : " + str(CSE21101124.age))
    print("Major     : " + CSE21101124.major)
    print("GPA       : " + str(CSE21101124.gpa))
    print("Probation : " + str(CSE21101124.is_on_probation))

elif st_name == 21101125:
    print("Name      : " + CSE21101125.name)
    print("Age       : " + str(CSE21101125.age))
    print("Major     : " + CSE21101125.major)
    print("GPA       : " + str(CSE21101125.gpa))
    print("Probation : " + str(CSE21101125.is_on_probation))

elif st_name == 21101126:
    print("Name      : " + CSE21101126.name)
    print("Age       : " + str(CSE21101126.age))
    print("Major     : " + CSE21101126.major)
    print("GPA       : " + str(CSE21101126.gpa))
    print("Probation : " + str(CSE21101126.is_on_probation))

else:
    print("Error!!! Can not find the student's information")