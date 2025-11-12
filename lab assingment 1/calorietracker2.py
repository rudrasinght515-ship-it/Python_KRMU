"""

Project: Calorie Tracker program (CLI)

Name: Rudra Singh
Roll No: 2501730339
Section: C

Description: 
      A easy program to record your daily intake calorie and help to compare it to needed calorie

"""

#*****************************

        # Step 1

#*****************************

print("==========**********==========")
print("Welcome to Calorie Tracker program")
print("==========**********==========\n")

print("Print your daily calorie intakeer")
print("Print your total and average calorie intake")
print("Print your daily calorie intake goal\n")

#*****************************

        # Step 2
        # Functions,input and data 

#*****************************

Meal = []
Calorie = []

Coll = input("To add meals press yes otherwise no: ").lower()

if Coll == "yes":
    Meal_no = int(input("\nHow many Meals do you want to add ? "))

    for i in range(Meal_no):
        print("\nMeal", i + 1)
        meal = input("Enter meal name: ")
        calorie = float(input("Enter calorie for this meal: "))

        Meal.append(meal)
        Calorie.append(calorie)

    print("\nYour meals and calories are saved")

else:
    print("\nOkay! Remember to find your needed calorie later.")

#*****************************

        # Step 3
        # Calorie average and calculations

#*****************************

Total_calories = sum(Calorie)
Average_calories = Total_calories/ len(Calorie)

Daily_need = float(input("\nEnter your daily calorie need: "))

print("\n------Calorie Report------ \n")
print("Total calories: ", Total_calories)
print("\nAverage pre meal: ", Average_calories)

if Total_calories <= Daily_need:
    print("\nYou are within your daily need calorie")
else:
    print("\nyou have exceeded you daily calorie need")

#*****************************

        # Step 4
        # Print Meal and calorie Data

#*****************************

print("\n--------Meal and Calorie Data-------\n")
print("Meal           Calorie\n")
for i in range(len(Meal)):
    print(Meal[i], "         ", Calorie[i], "\n")

print("Total Calories: ", Total_calories)
print("\nAverage Calories:  ", Average_calories, "\n")
 