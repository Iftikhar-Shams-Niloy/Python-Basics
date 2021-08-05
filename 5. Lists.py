# Lists and Tuples

# Lists:
print("\n>>>Lists : ")
names = ["Iftikhar", "Shams", "Niloy", "Toha", "Proma"]
print(type(names))
print(names)
#list[start:end:step]
#list[start:end]
#list[index no.]
print('1.',names[0]) # Prints the object at index no.0 (the 1st object)
print('2.',names[2]) # Prints the object at index no.2 (the 3rd object)
print('3.',names[1]) # Prints the object at index no.1 (the 2nd object)
print('4.',names[-1])# Prints the object that is 1st from the end.
print('5.',names[0:3]) # Prints the objects from index 0 to 2. It doesn't include index no.3.
print('6.',names[0:4:2])# Prints the first object then skips the second and goes to the third....
print('7.',names[::-1]) # Prints out the list in reverse

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
# CASE - 10
num_list = [1,4,2,5,6,7,4,3,2,1]

print(">>>",num_list,"<<<")
num_list.sort()
print("10.",end=" ")
print(num_list) # Sorts the number from small to large
#CASE - 11
num_list.reverse()
print("12.",num_list) # Reverses the list

# Getting Informations About the List:
print("\n>>> Getting Informations About the list")
roll_list = [12 , 23, 45, 24, 56 ,69, 102, 69, 121, 69] # This list contains 10 values
print("1.",len(roll_list)) # Prints out the length of the list (How many values it have, which is 5)
print("2.",roll_list.index(69))#Prints out the index position where the first 69 is situated from the left
print("3.",roll_list.count(69))#Prints out how many 69(s) are there in that list.

# Lists in a List:
print("\n>>> List in a List")
list_in_list = [["a","b","c"],[1,2,3],[True,False,None]]
print(">>>",list_in_list,"<<<")
print('1.',list_in_list[0])
print('2.',list_in_list[1][2])#Prints out the number 2 index of the second list(at index no.1)
list_in_list[1].append(4) #Appends a element in the list at index no.1
print('3.',list_in_list[1])
print("4.",list_in_list[2][1:])

# Using Operators With Lists:
print("\n>>>Using Operators With Lists")
list1 = [1,2,3,4,5]
list2 = [4,5,6,7,8]
list3 = [1,2,3]
print("1.",list1+list2) #Adds list2 elements in the end of list1 then prints
print("2.",list1*2) #Adds list1 elements in the end of list1 multiple times(Here it's 1 time) then prints
