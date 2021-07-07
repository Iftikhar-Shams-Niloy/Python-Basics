# range(stop) >>> automatically sets 'starting point' as 0 and 'step' as 1
# range(start, stop) >>> Automatically sets 'step' as 1
# range(start, stop, step) >>> set everything manually
A = list(range(10))
print(A)
B = list(range(5,10))
print(B)
C = list(range(2,10,2))
print(C)
D = list(range(1,10,-1)) #It will give you an empty list
# Cause this starts from 1 and can't step backwards. Cause 1 is the beginning number and the ending number is 10(It should have been opposite).
print(D)
E = list(range(10,0,-1)) #Assigns a list that starts at 10 ends at 1 (a reverse list)
print(E)
