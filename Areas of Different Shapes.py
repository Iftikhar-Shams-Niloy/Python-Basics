#Taking multiple inputs in a single variable. [also in a single line]
valor = input().split(" ")
A,B,C = valor
pi = 3.14159

#Calculation of different type of areas
area_triangular = (float(A)*float(C))/2
area_circle = pi*float(C)*float(C)
area_trapezium = ((float(A)+float(B))/2)*float(C)
area_square = float(B)*float(B)
area_rectangular = float(A)*float(B)

#Printing out the results
print("The area of triangle   : %.3lf" %area_triangular)
print("The area of circle     : %.3lf" %area_circle)
print("The area of square     : %.3lf" %area_square)
print("The area of trapezium  : %.3lf" %area_trapezium)
print("The area of rectangualr: %.3lf" %area_rectangular)