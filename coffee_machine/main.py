import resource


def is_resource_sufficient(items):
    for item in items:
        if items[item] >= resource.resources[item]:
            print(f"Insufficient resources: {item}")
            return False
    return True


is_on = True
money = 0
while is_on:
    choice = input("What would you like? (espresso, latte, cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resource.resources['Water']}")
        print(f"Milk: {resource.resources['Milk']}")
        print(f"Coffee: {resource.resources['Coffee']}")
        print(f"Money: {money}")
    else:
        drink = resource.MENU[choice]
        print(is_resource_sufficient(drink['ingredients']))
