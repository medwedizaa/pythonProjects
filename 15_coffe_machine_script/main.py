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


def is_enough_resources(res, ingredients):
    if res['water'] < ingredients['water']:
        print("Sorry there is not enough water.")
    elif 'milk' in ingredients and res['milk'] < ingredients['milk']:
        print("Sorry there is not enough milk.")
    elif res['coffee'] < ingredients['coffee']:
        print("Sorry there is not enough coffee.")
    else:
        return True
    return False


money = 0
run = True
while run:
    drink_type = input("What would you like? (espresso/latte/cappuccino): ")
    if drink_type == "off":
        break
    elif drink_type == "report":
        print(f"Water: {resources['water']}")
        print(f"Milk: {resources['milk']}")
        print(f"Coffee: {resources['coffee']}")
        print(f"Money: {money}")
        continue

    print("Please insert coins.")

    quarters = int(input("how many quarters?: "))  # 25¢
    dimes = int(input("how many dimes?: "))  # 10¢
    nickles = int(input("how many nickles?: "))  # 5¢
    pennies = int(input("how many pennies?: "))  # 1¢

    coin_sum = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
    drink_cost = MENU[drink_type]["cost"]
    drink_ingredients = MENU[drink_type]['ingredients']
    if coin_sum < drink_cost:
        print("Sorry that's not enough money. Money refunded.")
    else:
        if is_enough_resources(resources, drink_ingredients):
            money += drink_cost
            resources['water'] = resources['water'] - drink_ingredients['water']
            resources['coffee'] = resources['coffee'] - drink_ingredients['coffee']
            if 'milk' in drink_ingredients:
                resources['milk'] = resources['milk'] - drink_ingredients['milk']

            if coin_sum > drink_cost:
                print(f"Here is ${round(coin_sum - drink_cost, 2)} in change.")
            print(f"Here is your {drink_type} ☕️. Enjoy!")
    print("*" * 40)
