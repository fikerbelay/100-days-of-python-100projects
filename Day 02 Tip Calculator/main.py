print("Welcome to the tip calculator!")

Bill = float(input("What was the total bill? $"))
Tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
Number_of_people = int(input("How many people to split the bill? "))
Total_Per_person = ((Bill / Tip) + Bill) / Number_of_people

print("Each person should pay: " + " $" + str(Total_Per_person) )
