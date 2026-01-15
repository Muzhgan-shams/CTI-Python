# Pizza Deliveries
print("Welcome to Pizza Deliveries!")
pizza_size = input("What size pizza do you want? S, M, or L: ").strip().upper()
pepperoni = input(
    "Do you want pepperoni on your pizza? Y for Yes, N for NO: ").strip().upper()
extra_cheese = input("Do you want extra cheese? Y or N: ").strip().upper()
total_bill = 0

if pizza_size == "S":
    total_bill = 15
elif pizza_size == "M":
    total_bill = 20
elif pizza_size == "L":
    total_bill = 25
else:
    print("Missing Input. Try again.")
    exit()

# Pepperoni
if pepperoni == "Y":
    if pizza_size == "S":
        total_bill += 1
    else:
        total_bill += 2

# Extra cheese
if extra_cheese == "Y":
    total_bill += 1


print(f"Your final bill is ${total_bill}")
