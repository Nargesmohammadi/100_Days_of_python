# coffee machine
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
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

turn_off = 0

while turn_off != 1:
    user_choose = input("what would you like? ('espresso' / 'latte' / 'cappuccino':) or 'off' or 'report'\n")
    # user_chooses = input("How ")
    if user_choose == 'off':
        break
    if user_choose == 'report':
        print(resources)
    if user_choose in MENU:
        water_needed = MENU[user_choose]['ingredients']['water']
        milk_needed = MENU[user_choose]['ingredients']['milk']
        coffee_needed = MENU[user_choose]['ingredients']['coffee']
        if water_needed > resources['water']:
            print("Sorry, there isn't enough water.")
            break
        elif milk_needed > resources['milk']:
            print("Sorry, there isn't enough milk.")
            break
        elif coffee_needed > resources['coffee']:
            print("Sorry, there isn't enough coffee.")
            break


        # 3, 5, 2, 1
        coin_list = input("please insert coins. Type 'quarters:', 'dimes:', 'nickel:', 'pennies:'").split(", ")
        print(coin_list)
        quarter = float(coin_list[0])
        dimes = float(coin_list[1])
        nickel = float(coin_list[2])
        pennies = float(coin_list[3])

        my_money = 0.25 * quarter + 0.1 * dimes + 0.05 * nickel + 0.01 * pennies
        print(my_money)
        money_needed = MENU[user_choose]['cost']
        if money_needed > my_money:
            print("Sorry, That's not enough money. Money refused.")
            break
        elif my_money > money_needed:
            change = my_money - money_needed
            print(f"Here is {round(change, 2)}$ dollars.")
        resources['water'] -= MENU[user_choose]['ingredients']['water']
        resources['milk'] -= MENU[user_choose]['ingredients']['milk']
        resources['coffee'] -= MENU[user_choose]['ingredients']['coffee']
        if 'money' not in resources:
            resources['money'] = 0
        resources['money'] += money_needed

        print(f"Here's your{user_choose}. Enjoy! ")











