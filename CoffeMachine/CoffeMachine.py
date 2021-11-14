print("""Starting to make a coffee
Grinding coffee beans
Boiling water
Mixing boiled water with crushed coffee beans
Pouring coffee into the cup
Pouring some milk into the cup
Coffee is ready!""")
coffee_water = 200
coffee_milk = 50
coffee_beans = 15
water_m=int(input("Write how many water we got in machine"))
milk_m=int(input("Write how many milk we got in machine"))
beans_m=int(input("Write how many beans we got in machine"))
k_cups = int(input("Write how many cups of coffee you will need:"))
cup_water = water_m // coffee_water
cup_milk = milk_m // coffee_milk
cup_beans = beans_m // coffee_beans
number = min([cup_water, cup_milk, cup_beans])
if number == k_cups:
    print("Yes, I can make that amount of coffee")
elif number > k_cups:
    print("Yes, I can make that amount of coffee (and even " + str(number - k_cups) + " more than that)")
else:
    print("No, I can make only " + str(number) + " cups of coffee")


















# water = k_cups * coffee_water
# milk = k_cups * coffee_milk
# beans = k_cups * coffee_beans
# print('For ' + str(k_cups) + ' cups of coffee you will need:')
# print(str(water) + ' ml of water')
# print(str(milk) + ' ml of milk')
# print(str(beans) + ' g of coffee beans')

