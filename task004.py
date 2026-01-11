# Split the Bill
print("Welcome to Split the Bill!")

bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? (10, 12, or 15): "))
split = int(input("How many people are splitting the bill? "))

tip_amount = bill * tip / 100
total_bill = bill + tip_amount
each_person = total_bill / split

print(f"Each person should pay: ${each_person}")
