salary = int(input("What is your annual salary? "))

if salary < 150000:
    print("You are excluded from taxation")

elif salary >= 150000 and salary <= 1500000:
    print("Your tax rate is 15%")
    print("ie", int(salary*0.15))
    print("Thus your salary is", int(salary +(-salary*0.15)))

elif salary >= 1500000 and salary <= 3000000:
    print("Your tax rate is 23%")
    print("ie", int(salary*0.23))
    print("Thus your salary is", int(salary +(-salary*0.23)))

else:
    print("Your tax rate is 35%")
    print("ie", int(salary*0.35))
    print("Thus your salary is", int(salary +(-salary*0.35)))