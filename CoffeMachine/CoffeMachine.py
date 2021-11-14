# print("""Starting to make a coffee
# Grinding coffee beans
# Boiling water
# Mixing boiled water with crushed coffee beans
# Pouring coffee into the cup
# Pouring some milk into the cup
# Coffee is ready!""")
# coffee_water = 200
# coffee_milk = 50
# coffee_beans = 15
# water_m=int(input("Write how many water we got in machine"))
# milk_m=int(input("Write how many milk we got in machine"))
# beans_m=int(input("Write how many beans we got in machine"))
# k_cups = int(input("Write how many cups of coffee you will need:"))
# cup_water = water_m // coffee_water
# cup_milk = milk_m // coffee_milk
# cup_beans = beans_m // coffee_beans
# number = min([cup_water, cup_milk, cup_beans])
# if number == k_cups:
#     print("Yes, I can make that amount of coffee")
# elif number > k_cups:
#     print("Yes, I can make that amount of coffee (and even " + str(number - k_cups) + " more than that)")
# else:
#     print("No, I can make only " + str(number) + " cups of coffee")

# print("""Starting to make a coffee
# Grinding coffee beans
# Boiling water
# Mixing boiled water with crushed coffee beans
# Pouring coffee into the cup
# Pouring some milk into the cup
# Coffee is ready!""")
# coffee_water = 200
# coffee_milk = 50
# coffee_beans = 15
# machie_water=400
# machine_milk=540
# machine_beans=120
# machine_1cups=9
# machine_money=550
#
#
# print("The coofe machine has: /n (machine_water) of Water /n (machine_beans) of beans /n")
#
#
# vibor=print("Write action- Buy'Fill'take")
# if vibor==Buy:
#     coffe_vibor=print("What do you want to buy 1-espresso 2-latte 3-Cappuccino:")
#     if coffe_vibor==1:

water = 400
milk = 540
beans = 120
cups = 9
money = 550

def content():
    print('The coffee machine has:')
    print(str(water) + ' of water')
    print(str(milk) + ' of milk')
    print(str(beans) + ' of coffee beans')
    print(str(cups) + ' of disposable cups')
    print(str(money) + ' of money' )


content()
print("")

def buy():
    print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:')
    global water
    global milk
    global beans
    global money
    global cups
    type_coffe = int(input())
    if type_coffe == 1:
        water -= 250
        beans -= 16
        cups -= 1
        money += 4
    elif type_coffe == 2:
        water -= 350
        milk -= 75
        beans -= 20
        cups -= 1
        money += 7
    elif type_coffe == 3:
        water -= 200
        milk -= 100
        beans -= 12
        cups -= 1
        money += 6


def fill():
    global water
    global milk
    global beans
    global money
    global cups
    print("Write how many ml of water you want to add:")
    fill_water = int(input())
    water += fill_water
    print("Write how many ml of milk you want to add:")
    fill_milk = int(input())
    milk += fill_milk
    print("Write how many grams of coffee beans you want to add:")
    fill_beans = int(input())
    beans += fill_beans
    print("Write how many disposable coffee cups you want to add:")
    fill_cups = int(input())
    cups += fill_cups


def take():
    global money
    print("I gave you " + str(money) + "\n")
    money = 0


def action():
    print('Write action (buy, fill, take):')
    user_action = input()
    if user_action == 'buy':
        buy()
        content()
    elif user_action == 'fill':
        fill()
        content()
    elif user_action == 'take':
        take()
        content()


action()



















# water = k_cups * coffee_water
# milk = k_cups * coffee_milk
# beans = k_cups * coffee_beans
# print('For ' + str(k_cups) + ' cups of coffee you will need:')
# print(str(water) + ' ml of water')
# print(str(milk) + ' ml of milk')
# print(str(beans) + ' g of coffee beans')

