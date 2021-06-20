# Lists and Tuples

# Lists:
print("\n>>>Lists : ")
names = ["Iftikhar", "Shams", "Niloy", "Toha", "Proma"]
print(type(names))
print(names)
print(names[0]) # Prints the object at index no.0 (the 1st object)
print(names[2]) # Prints the object at index no.2 (the 3rd object)
print(names[1]) # Prints the object at index no.1 (the 2nd object)
print(names[-1])# Prints the object that is 1st from the end.
print(names[0:3]) # Print the objects from index 0 to 2. It doesn't include index no.3.
print(names[::-1]) # Prints out the list in reverse

# Modifying a List:
print("\n>>>Modifying a List : ")
# CASE - 1
print("1.",end=" ")
names[1] = "Ismail" # Changes the object at index no.1 with a new value
print(names)
# CASE - 2
print("2.",end=" ")
names[4] = 20 # Changes the object at index no.4 with a new value
print(names)
# CASE - 3
print("3.",end=" ")
names.insert(1,"NEW Shams") # Inserts a new value at index no.1
print(names)
# CASE - 4
print("4.",end=" ")
names.append("NEW Niloy") # Inserts a new value in the end of the list
print(names)
# CASE - 5
print("5.",end=" ")
names.pop() # Clears the last value of the list
print(names)
# CASE - 6
print("6.",end=" ")
names.remove("Toha") # Clears a specific value/object you want to clear from the list
print(names)
# CASE - 7
print("7.",end=" ")
new_names = ["NEW Toha", "NEW Proma", "NEW Ismail"] # making a new list
names.extend(new_names) # Adds a list (new_names) contents
print(names)
# CASE - 8
print("8.",end=" ")
copy_list = names.copy() # Assigns a list into another
print(copy_list)
# CASE - 9
print("9.",end=" ")
names.clear() # Clears ALL the values/objects in a list (Makes it a null list)
print(names)

# Getting Informations About the List:
print("\n>>> Getting Informations About the list")
roll_list = [12 , 23, 45, 24, 56] # This list contains 5 values
print(len(roll_list)) # Prints out the length of the list (How many values it have, which is 5)

#Tuples :
print("\n>>> Tuples : ")
names2 = ("Niloy", "Shams", "Iftikhar")
# tuples are lists but you can't modify them
# Tuples are immutable
print(type(names2))
print(names2)
print(names2[1])
# If we try to modify or change a tuple, the program will going to break and show an error!!!
