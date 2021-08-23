# Dictonary:
''' To create a dictionary , you need to use {}
and 2 kinds of item 1.Key & 2.Value ...
After making the dictionary, we can find the
value just using the keyword!!!
'''
#Basic :
print("\n>>> Basic:")
dictionary1 = {1:"Niloy", 2:"Shams", 3:"Iftikhar"}
print(dictionary1[1])
print(dictionary1[2])
#print(dictinary1["Iftikhar"])
# You can't use the value to find the key!!!

# Using user input in the dictionary :
print("\n>>>Using user input in the dictionary:")
dictionary2 = {
    "Apple" : "Red",
    "Mango" : "Yellow",
    "Jackfruit" : "Green",
    "Lichi" : "Red",
    "Banana" : "Yellow",
    "Grapes" : "Color varies from ",
    "Orange" : "Orange"
}
fruit_name = input("Enter a fruit name:")
print("Fruit Color:",dictionary2[fruit_name])

# Modifying Dictonary :
print("\n>>> Modifying Dictonary:")
dictionary3 = {"name":"Niloy", "roll" : 21101124}
print(dictionary3)
print(dictionary3["roll"]) #Printing roll before modifying
dictionary3["roll"] = 5916
print(dictionary3)
print(dictionary3["roll"]) #Printing roll after modifying
dictionary3["college roll"] = 10748 # Adding new item !!!
print(dictionary3)
my_dict1 = (dictionary3.popitem()) # Pops out the last element in th dictionary.
my_dict2 = dictionary3.clear() #Clears everything from the list!
print(my_dict1)
print(my_dict2)

# List inside Dictionary :
print("\n>>> List inside Dictionary:")
dictionary4 = {1 : [1,2,3], 2 : [4,5,6]}
print(dictionary4[1])
print(dictionary4[2])
print(dictionary4[1][2])#getting access of the list inside the dictionary key:1
print(dictionary4[2][1])#getting access of the list inside the dictionary key:2

###Using for loop with a dictionary :
print("\n>>> Using for loop with a dictionary:")
dictionary5 = {1:"Niloy",2:"Shams",3:"Ismail"}
for key in dictionary5:
    print("Dictionary Keys :",key)
print()
for items in dictionary5.items():
    print("Dictionary Items :",items)
print()
for key,value in dictionary5.items():
    print("Dictionary Keys :",key,"| Dictionary Values:",value)
print()
for values in dictionary5.values():
    print("Dictionary Values:",values)

###Changing dictionary :
dictionary6 = {1:"N",2:"I",3:"L",4:"O",5:"Y"}
dictionary6_1 = dictionary6
dictionary6_2 = dictionary6.copy()
#Printing all three dictionaries
print("dictionary6 :",dictionary6)
print("dictionary6_1 :",dictionary6_1)
print("dictionary6_2 :",dictionary6_2)
#Modifying dictionary6_1
print()
print("Modifying dictionary6_1:")
print("Step-1:",dictionary6_1)
print("Step-2:",dictionary6_1.values())
print("Step-3:",dictionary6_1.popitem())
print("Step-4:",dictionary6_1)
print("Step-5:",dictionary6_1.pop(1))
print("Final :",dictionary6_1)
#Modifying dictionary6_1
print()
print("Modifying dictionary6_2:")
dictionary6_2.values()
dictionary6_2.pop(1)
dictionary6_2.pop(2)
dictionary6_2.pop(3)
print("Final :",dictionary6_1)
#Again printing all three dictionaries
print()
print("dictionary6 :",dictionary6)
print("dictionary6_1 :",dictionary6_1)
print("dictionary6_2 :",dictionary6_2)
'''So we can see that as we modified dictionary6_1, dictionary6 also changed.
This happens because we didn't use the .copy() function. Now, we notice that
for dictionary6_2 nothing has changed in dictionary6'''

#Taking dictionary as input (Using Loops) :
print("\n>>> Taking dictionary as input (Using Loops)")
dictionary7 = {}
n = int(input("How many key-value pairs do you want to add?"))
for i in range(n):
    key1 = input("Enter key:")
    value1 = input("Enter value:")
    dictionary7[key1] = value1
print("dictionary7 :",dictionary7)

#Taking dictionary as input in a single line:
print("\n>>> Taking dictionary as input in a single line")
user_input = input("Enter (key:value) pairs using coma(,) :")
dictionary8 = {}
list1 = user_input.split(",")
for items in list1:
    a,b = items.split(":")
    dictionary8[a] = b
print("dictionary8 :",dictionary8)
