MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0
status = True


def is_resources_sufficient(drink):
    for item in drink:
        if drink[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True


def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: {profit}")


def process_coin():
    """Return total of coins"""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def is_payment_successful(coin, cost):
    if coin < cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    elif coin >= cost:
        global profit
        profit += cost
        print(f"Here is the change $ {round(coin - cost, 2)}")
        return True


def make_coffee(drink, ingredients):
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your {drink}")


while status:
    user_input = input("What would you like? (espresso/latte/cappuccino):").lower()

    if user_input == "report":
        report()

    elif user_input == "off":
        status = False

    else:
        drink = MENU[user_input]
        if is_resources_sufficient(drink["ingredients"]):
            payment = process_coin()
            if is_payment_successful(payment, drink["cost"]):
                make_coffee(user_input, drink["ingredients"])
