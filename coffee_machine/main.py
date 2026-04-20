import resource


def is_resource_sufficient(items):
    for item in items:
        if resource.resources[item] < items[item]:
            print(f"Insufficient resources: {item}")
            return False
    return True


def process_coin():
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total


profit = 0


def is_transaction_successful(received, cost):
    if received >= cost:
        change = round(received - cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += cost
        return True
    else:
        print("Sorry, that is not enough money. Money refunded.")
        return False


def make_coffee(drink, order_items):
    for item in order_items:
        resource.resources[item] -= order_items[item]
    print(f"Here is your {drink}. Enjoy!")


print(resource.coffee_logo)

is_on = True
while is_on:
    choice = input(
        "What would you like? (espresso, latte, cappuccino): ").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resource.resources['water']}ml")
        print(f"Milk: {resource.resources['milk']}ml")
        print(f"Coffee: {resource.resources['coffee']}g")
        print(f"Money: ${profit}")
    elif choice in resource.MENU:
        drink = resource.MENU[choice]
        if is_resource_sufficient(drink['ingredients']):
            payment = process_coin()
            if is_transaction_successful(payment, drink['cost']):
                make_coffee(choice, drink["ingredients"])
    else:
        print("Invalid choice. Please select espresso, latte, or cappuccino.")
