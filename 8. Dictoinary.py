# Dictonary:
''' To create a dictionary , you need to use {}
and 2 kinds of item 1.Key & 2.Value ...
After making the dictionary, we can find the
value just using the keyword!!!
'''
# Example 1(Basic):
print("\n>>> Example-1:")
dictionary1 = {1:"Niloy", 2:"Shams", 3:"Iftikhar"}
print(dictionary1[1])
print(dictionary1[2])
#print(dictinary1["Iftikhar"])
# You can't use the value to find the key!!!

# Example 2(Taking user input):
print("\n>>> Exmaple-2:")
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

# Example 3(Modifying Dictonary):
print("\n>>> Example-3:")
dictionary3 = {"name":"Niloy", "roll" : 21101124}
print(dictionary3)
print(dictionary3["roll"]) #First print
dictionary3["roll"] = 5916
print(dictionary3)
print(dictionary3["roll"]) #second one to know if the
dictionary3["college roll"] = 10748 # Adding new item !!!
print(dictionary3)
my_dict1 = (dictionary3.popitem()) # Pops out the last element in th dictionary.
my_dict2 = dictionary3.clear() #Clears everything from the list!
print(my_dict1)
print(my_dict2)

# Example 4(List inside Dictionary) :
print("\n>>> Example 4:")
dictionary4 = {1 : [1,2,3], 2 : [4,5,6]}
print(dictionary4[1])
print(dictionary4[2])