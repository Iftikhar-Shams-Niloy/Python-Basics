
gender = input("Are you a Male or Female? :")

if gender == "Male":
    print("So, you are a Male")
    bmi1= input("Do you want to know your BMI?(Yes/No):")

    if bmi1 == "Yes" :
        male_height = float(input("What is your height(cm)?:"))
        male_weight = float(input("What is your weight(kg)?:"))
        male_height_meter= male_height/100
        male_bmi = male_weight / (male_height_meter * male_height_meter)

        print("Your BMI is :",float (male_bmi))
#Make a review option
#Make a BMR option
#Make the Female section
#Complete any unfinished part
