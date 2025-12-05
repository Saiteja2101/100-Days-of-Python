
# Coffee Machine Program (simple / amateur version)

# menu with ingredients and cost
MENU = {
    "espresso": {
        "ingredients": {"water": 50, "milk": 0, "coffee": 18},
        "cost": 1.5
    },
    "latte": {
        "ingredients": {"water": 200, "milk": 150, "coffee": 24},
        "cost": 2.5
    },
    "cappuccino": {
        "ingredients": {"water": 250, "milk": 100, "coffee": 24},
        "cost": 3.0
    }
}

# starting resources
resources = {
    "water": 1000,
    "milk": 500,
    "coffee": 100,
    "money": 0
}

def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")

def check_resources(drink):
    ingredients = MENU[drink]["ingredients"]
    for item in ingredients:
        if ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def process_coins():
    print("Please insert coins.")
    q = int(input("How many quarters?: "))
    d = int(input("How many dimes?: "))
    n = int(input("How many nickles?: "))
    p = int(input("How many pennies?: "))
    total = q * 0.25 + d * 0.10 + n * 0.05 + p * 0.01
    return total

def make_coffee(drink):
    ingredients = MENU[drink]["ingredients"]
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your {drink}. Enjoy!")

# main loop
machine_on = True

while machine_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")

    if choice == "off":
        machine_on = False

    elif choice == "report":
        print_report()

    elif choice in MENU:
        # check resources
        if check_resources(choice):
            payment = process_coins()
            drink_cost = MENU[choice]["cost"]
            if payment < drink_cost:
                print("Sorry that's not enough money. Money refunded.")
            elif payment > drink_cost:
                change = payment - drink_cost
                print(f"Here is ${change} in change.")
                resources["money"] += drink_cost
                make_coffee(choice)
            elif payment == drink_cost:
                resources["money"] += drink_cost
                make_coffee(choice)

    else:
        print("Invalid selection.")

