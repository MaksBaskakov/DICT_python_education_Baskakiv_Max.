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

latte_water = 350
latte_milk = 75
latte_beans = 20

cappucino_water = 200
cappucino_milk = 100
cappucino_beans = 12

espresso_water = 250
espresso_beans = 16

tupa_1 = 1

cupLatte_water = water // latte_water
cupLatte_milk = milk // latte_milk
cupLatte_beans = beans // latte_beans
numberLatte = min(cupLatte_water, cupLatte_milk, cupLatte_beans)

cupCappucino_water = water // cappucino_water
cupCappucino_milk = milk // cappucino_milk
cupCappucino_beans = beans // cappucino_beans
numberCappucino = min(cupCappucino_water, cupCappucino_milk, cupCappucino_beans)

cupEspresso_water = water // espresso_water
cupEspresso_beans = beans // espresso_beans
numberEspresso = min(cupEspresso_water, cupEspresso_beans)


class CoffeMachine:
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.cups = 9
        self.money = 550

def content(self):
    print('The coffee machine has:')
    print(str(self.water) + ' of water')
    print(str(self.milk) + ' of milk')
    print(str(self.beans) + ' of coffee beans')
    print(str(self.cups) + ' of disposable cups')
    print(str(self.money) + ' of money')
    # CoffeMachine.content()

def buy(self):
    global water
    global milk
    global beans
    global money
    global cups
    global numberEspresso
    global numberLatte
    global numberCappucino
    global tupa_1

    cupLatte_water = water // latte_water
    cupLatte_milk = milk // latte_milk
    cupLatte_beans = beans // latte_beans
    numberLatte = min(cupLatte_water, cupLatte_milk, cupLatte_beans)

    cupEspresso_water = water // espresso_water
    cupEspresso_beans = beans // espresso_beans
    numberEspresso = min(cupEspresso_water, cupEspresso_beans)

    cupCappucino_water = water // cappucino_water
    cupCappucino_milk = milk // cappucino_milk
    cupCappucino_beans = beans // cappucino_beans
    numberCappucino = min(cupCappucino_water, cupCappucino_milk, cupCappucino_beans)

    print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino 4-go back to main menu:')

    type_coffe = int(input())
    if type_coffe == 1:
        if numberEspresso >= tupa_1 and cups >= 1:
            print('Sha sdelaem')
            self.water -= 250
            self.beans -= 16
            self.cups -= 1
            self.money += 4
        else:
            print('Ne hvataet')
    elif type_coffe == 2:
        if numberLatte >= 1 and cups >= 1:
            print(numberLatte)
            print('SHa sdelaem')
            self.water -= 350
            self.milk -= 75
            self.beans -= 20
            self.cups -= 1
            self.money += 7
        else:
            print("Ne hvataet")
    elif type_coffe == 3:
        if numberCappucino >= tupa_1 and cups >= 1:
            print("Sha sdelaem")
            self.water -= 200
            self.milk -= 100
            self.beans -= 12
            self.cups -= 1
            self.money += 6
        else:
            print('Ne hvataet')
    elif type_coffe == 4:
        action(object)

def fill(self):
    global water
    global milk
    global beans
    global money
    global cups
    print("Write how many ml of water you want to add:")
    fill_water = int(input())
    self.water += fill_water
    print("Write how many ml of milk you want to add:")
    fill_milk = int(input())
    self.milk += fill_milk
    print("Write how many grams of coffee beans you want to add:")
    fill_beans = int(input())
    self.beans += fill_beans
    print("Write how many disposable coffee cups you want to add:")
    fill_cups = int(input())
    self.cups += fill_cups

def take(self):
    print("I gave you " + str(self.money) + "\n")
    self.money = 0

def exit():
    print('Glhf')

def action(object):
    print('Write action (buy, fill, take, remaining, exit):')
    user_action = input()
    if user_action == 'buy':
        buy(object)
        action(object)
    elif user_action == 'fill':
        fill(object)
        action(object)
    elif user_action == 'exit':
        exit()

    elif user_action == 'remaining':
        content(object)
        action(object)
    elif user_action == 'take':
        take(object)
        action(object)


CM = CoffeMachine()
action(CM)
# water = k_cups * coffee_water
# milk = k_cups * coffee_milk
# beans = k_cups * coffee_beans
# print('For ' + str(k_cups) + ' cups of coffee you will need:')
# print(str(water) + ' ml of water')
# print(str(milk) + ' ml of milk')
# print(str(beans) + ' g of coffee beans')
