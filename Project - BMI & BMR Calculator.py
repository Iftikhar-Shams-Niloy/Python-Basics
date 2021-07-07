bmi1= input("Do you want to know your BMI?(Yes/No):")
#BMI CALCULAOR
if bmi1 == "Yes":
    real_height = float(input("What is your height(cm)?:"))
    real_weight = float(input("What is your weight(kg)?:"))
    real_height_meter = real_height / 100
    real_bmi = real_weight / (real_height_meter * real_height_meter)
    print("Your BMI is :", float(real_bmi))
    review = input("\nDo you want a Review on your health condition?: (Yes/No):")
#BMR Calculator
    if review == "Yes":
        if real_bmi <= 18.5:
            print('''You are underweight. You need to gain weight by eating healthy foods.
            Eat a lot, exercise and avoid bad habbits. ''')
        elif real_bmi >= 18.5 and real_bmi <= 24.9:
            print('''You have normal weight.Keep your healthy diet as it is.''')
        elif real_bmi >= 25 and real_bmi <= 29.9 :
            print("You are over weight. Need to exercise daily.Avoid fast foods, soft drinks.\n Eat a lot of fruits and vegitables.Drink a lot of water.")
        elif real_bmi >= 30 :
            print("You are suffering from obesity. You may suffer some serious health issues.\n Workout a lot. Never even try to eat any unheathy food. \n Need to see a doctor.")

elif bmi1 == "No":
    print("Okay! But we also have BMR calculator. Do ")
else:
    print("Invalid Input!!!")
    
ask = input("\nDo you want to know your BMR?(Yes/No) :")
if ask == "Yes":

    gender = input("\nAre you a Male or Female? :")

    if gender == "Male":
        print("So, you are a Male!!!")
        male_height = float(input("What is your height?(cm) :"))
        male_weight = float(input("What is your weight?(kg) :"))
        male_age = float(input("What is your age?(years) :"))
        male_bmr = 66.47 + (13.75*male_weight) + (5.003*male_height)-(6.755*male_age)
        print("Your BMR is :", male_bmr)

        male_calories = input("\nDo you want to know how much calories you burn a day?(Yes/No) :")
        if male_calories == "Yes":
            male_choice = int(input('''How much do you exercise?:
            1.Little exercise or no exercise.
            2.Light exercise/sports 1-3 days/week.
            3.Moderatetely active (moderate exercise/sports 3-5 days/week).
            4.Very active (hard exercise/sports 6-7 days a week).
            5.extra active (very hard exercise/sports & physical job or 2x training).
            --->>>'''))
            if male_choice == 1 :
                print("You need to burn ",male_bmr*1.2 ," calories everyday.")
            if male_choice == 2 :
                print("You need to burn ",male_bmr*1.375 ," calories everyday.")
            if male_choice == 3 :
                print("You need to burn ",male_bmr*1.55 ," calories everyday.")
            if male_choice == 4 :
                print("You need to burn ",male_bmr*1.725 ," calories everyday.")
            if male_choice == 5 :
                print("You need to burn ",male_bmr*1.9 ," calories everyday.")

    elif gender == "Female":
        print("So, you are a Female!!!")
        female_height = float(input("What is your height?(cm) :"))
        female_weight = float(input("What is your weight?(kg) :"))
        female_age = float(input("What is your age?(years) :"))
        female_bmr = 655.1 + (9.563*female_weight) + (1.85*female_height) - (4.674* female_age)
        print("Your BMR is :", female_bmr)

        female_calories = input("\nDo you want to know how much calories you burn a day?(Yes/No) :")
        if female_calories == "Yes":
            female_choice = int(input('''How much do you exercise?:
            1.Little exercise or no exercise.
            2.Light exercise/sports 1-3 days/week.
            3.Moderatetely active (moderate exercise/sports 3-5 days/week).
            4.Very active (hard exercise/sports 6-7 days a week).
            5.extra active (very hard exercise/sports & physical job or 2x training).
            --->>>'''))
            if female_choice == 1 :
                print("You need to burn ",female_bmr*1.2 ," calories everyday.")
            if female_choice == 2 :
                print("You need to burn ",female_bmr*1.375 ," calories everyday.")
            if female_choice == 3 :
                print("You need to burn ",female_bmr*1.55 ," calories everyday.")
            if female_choice == 4 :
                print("You need to burn ",female_bmr*1.725 ," calories everyday.")
            if female_choice == 5 :
                print("You need to burn ",female_bmr*1.9 ," calories everyday.")

        female_bmr = 88.362 + (13.397*female_weight) + (4.799*female_height)-(5.677*female_age)
        
elif ask == "No":
    print("As you wish! Have a nice day... (^_^) ")

else:
    print("Invalit Input!!!")
