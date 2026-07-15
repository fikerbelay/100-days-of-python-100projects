print("Welcome to the tip calculator!")

Bill = float(input("What was the total bill? $"))
Tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
Number_of_people = int(input("How many people to split the bill? "))

Total_amount = ((Bill / Tip) + Bill)
Total_Per_person = round( Total_amount / Number_of_people, 2)

print(f"Each person should pay: ${Total_Per_person}")
