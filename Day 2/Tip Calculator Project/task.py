print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
tip_percentage = tip / 100
total_bill = bill + (bill * tip_percentage)
each_person_amount = round(total_bill / people, 2)
formated_individual_amount = "%0.2f" % each_person_amount
print(f"Each person should pay ${formated_individual_amount}")
