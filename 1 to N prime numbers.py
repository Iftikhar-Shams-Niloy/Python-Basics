
#This program print all the prime number from 1 to N. Where N is an input

while(1):
    try :
        N = int(input("### Know the prime numbers from 1 to N ### \n N = ? : "))
    except (ValueError):
        print("Error!!! Invalid input!!!\n")
        continue

    x = 5
    print("The Prime Numbers Are :")
    if N <= 2 :
        print("2")
    elif N <= 3 :
        print("2")
        print("3")
    elif N >= 5 :
        print("2")
        print("3")
        print("5")
    elif N == 1:
        print("***None***")
    else:
        print("Error!!! Invalid input!!!")

        print("2")
    for x in range(x,N+1):
        if x%2 == 0 or x%3==0 or x%5==0  :
            continue
        else:
            print(x)
        x=x+1
