#optimal weight for men and women. Equal to their height for men (minus 100), -5 kilos of their height for women

gender = input("What is your sex? (m/f) ")

if gender != "m" and gender != "f":
    print("Invalid parameter")
    exit(0)

height = int(input("What is your height? (in cm) "))

if height < 100 or height > 200:
    print("You are either too tall or too short for this machine")
    exit(0)

weight = int(input("What is your weight? (in kg) "))

optimal_weight = 0

if gender == "m":
    optimal_weight = height - 100
    print("Your optimal weight is", optimal_weight, "kg")
    if optimal_weight != weight:
        print("You need to lose", weight - optimal_weight, "kg")
    else:
        print("You are at your optimal weight")

elif gender == "f":
    optimal_weight = height - 105
    print("Your optimal weight is", optimal_weight, "kg")
    if optimal_weight != weight:
        print("You need to lose", weight - optimal_weight, "kg")
    else:
        print("You are at your optimal weight")