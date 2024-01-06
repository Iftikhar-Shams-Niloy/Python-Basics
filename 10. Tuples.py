#Tuples :
"""A tuple is a collection of objects/values that is separated
by commas. Tuples are similar to list in many ways. Lists are
mutable but tuples are immutable(We can not change anything inside a tuple)."""
print("\n>>> Tuples : ")
tuple1 = ("Niloy", "Shams", "Iftikhar")
# tuple have characteristics like list but you can't modify them
# Tuples are immutable
print(type(tuple1))
print("tuple1:",tuple1)
print("tuple1[1]:",tuple1[1])
# If we try to modify or change a tuple, the program will going to break and show an error!!!
#How to use a tuple:
print()
#CASE 1:
tuple2 = 1,2,3,4,5,5,5,"Niloy","Shams"
print("tuple2:",tuple2) #to make a tuple using parentheses is optional
# Find the length of a tuple:
print("the length of a tuple:",len(tuple2))
# Printing a tuple in reverse (Nothing changed inside tuple2):
print("1.Reversed :",tuple(reversed(tuple2)))
print("2.Reversed :",tuple2[::-1])
# Getting the index of a value:
print(">>>Index position of 'Niloy':",tuple2.index("Niloy"))#Gives us the index position of "Niloy" in the tuple
print(">>>How many 5 are in tuple2 :",tuple2.count(5))
#Slicing a tuple:
#tuple2[START : STOP : STEP]
print()
'''If we don't determine:
1.any start value,the program automatically take that as 0
2.any stop value, the program automatically take that as the highest index or you may say -1
3.any step value, the program automatically take that as 1'''
print("Case-1:",tuple2[1:5]) #Starts from index 1 and stops at index 5
print("Case-2:",tuple2[1:9:2]) #Starts from index 1 and stops at index 9 skipping over every 1 values in between
print("Case-3:",tuple2[:5:3]) #Starts from index 0 and stops at index 5 skipping over every 2 values in between
print("Case-4:",tuple2[::-2]) # Starts from index -2 and prints the tuple in reverse skipping over every 2 values.
#Assigning the values of tuples in different variables:
print()
tuple3 = (21,22,23)
num1,num2,num3 = tuple3
print("tuple3:",tuple3)
print(num1)
print(num2)
print(num3)
#**If we give less or more variable than the number of elements in the list, it will going to throw an error.

#Coping a tuplet to a list:
my_list = list(tuple3)
print("my_list:",my_list)

#Accessing tuple using for loop:
print()
#Case-1:
tuple4 = 1,2,3,4,5
print("tuple4 :",tuple4)
for i in tuple4:
    print(i)
#Case-2:
print()
for j in tuple4:
    if j <= 3 :
        print(j)
    else:
        print("Not less than 3!!!")
