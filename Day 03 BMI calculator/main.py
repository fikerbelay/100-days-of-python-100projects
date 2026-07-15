print("Welcome to BMI calculator!")

height = float(input("What is your height in meters? "))
weight = float(input("What is your weight in kilograms? "))

BMI = weight / (height ** 2)

if BMI < 18.5:
    print("You are underweight")
elif 25 > BMI >= 18.5:
    print("You are normal weight")
else:
    print("You are overweight")