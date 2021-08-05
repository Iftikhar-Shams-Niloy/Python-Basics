# Sets :
'''Sets are unordererd collection of
unique elements. There can only be one
representative of the same objects.
You need to use {} to make a set inside
a variable'''

'''When you enter some numbers in set,
it's get sorted automatically'''
print("\n>>> Example 1:")
myset1 = {1,2,3,4,7,6,5}
print(myset1)
print(type(myset1))

'''If you enter string values in set,
It does not sort it. But, it also prints
the strings in the list in random manner.'''
print("\n>>> Example 2:")
myset2 = {"A","C","B","c","a","b"}
print(myset2)
#print(myset2[1]) <- this will show as an error in the code.

'''You can not have the same object
more than once in a set.'''
print("\n>>> Example 3:")
myset3 = {1,1,2,2,3,3,4,4}
print(myset3)

#I can convert a list into a set:
print("\n>>>Example 4:")
mylist = ["A","A",15,15,12,13,15,11,12]
print(mylist)
print(type(mylist))
myset4 = set(mylist) #Converting the list into a set!
print(myset4)
print(type(myset4))

# Booleans :
print("\n*** BOOLEANS ***")
'''Booleans are operator that allow
you to convey True or False statements.
It's essential when we will deal with
control flow.'''
gender_male = True
hieght_tall = False
print(">>>Exmaple 5:")
print(gender_male)
print(hieght_tall)
print(">>>Example 6:")
print(1 == 1)
print(1 > 2)
print(1 < 2)
print(">>>Example 7:")
test1 = "A"
test2 = "AAA"
print(test1 > test2)
print(test1 < test2)
print(">>>Example 8:")
test3 = [1,2,3]
test4 = [1,2,3,4,5]
print(test4 > test3)
print(test4 < test3)
'''Booleans(True/False) are the
 only keywords in python, that 
 starts with an uppercase letter'''
