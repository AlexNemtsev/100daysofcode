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

money = 0.0
is_active = True

def check_resources(drink):
    ingredients = MENU[drink]["ingredients"]
    enough_resources = True
    for ingredient in ingredients:
        if resources[ingredient] < ingredients[ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            enough_resources = False
    return enough_resources


def proceed(quarters, dimes, nickels, pennies):
    return quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01


def is_transaction_succeed(cost, inserted):
    if inserted >= cost:
        return True
    else:
        return False

def make_drink(drink):
    ingredients = MENU[drink]["ingredients"]
    for ingredient in ingredients:
        resources[ingredient] -= ingredients[ingredient]

while is_active:
    drink = input('What would you like? (espresso/latte/cappuccino): ')

    if drink == 'off':
        is_active = False

    elif drink == 'report':
        print(f'Water: {resources["water"]}ml')
        print(f'Milk: {resources["milk"]}ml')
        print(f'Coffee: {resources["coffee"]}g')
        print(f'Money: ${money}')

    else:
        if check_resources(drink):
            print('Please insert coins.')
            quarters = int(input('how many quarters?: '))
            dimes = int(input('how many dimes?: '))
            nickels = int(input('how many nickels?: '))
            pennies = int(input('how many pennies?: '))

            inserted = proceed(quarters, dimes, nickels, pennies)
            cost = MENU[drink]["cost"]

            if is_transaction_succeed(cost, inserted):
                make_drink(drink)
                money += cost
                if inserted > cost:
                    print(
                        f'Here is ${round(inserted - cost, 2)} dollars in change.')
                print(f'Here is your {drink}. Enjoy!')
            else:
                print("Sorry that's not enough money. Money refunded.")
