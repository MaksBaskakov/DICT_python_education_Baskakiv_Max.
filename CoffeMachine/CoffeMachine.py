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
k_cups = int(input("Write how many cups of coffee you will need:"))
water = k_cups * coffee_water
milk = k_cups * coffee_milk
beans = k_cups * coffee_beans
print('For ' + str(k_cups) + ' cups of coffee you will need:')
print(str(water) + ' ml of water')
print(str(milk) + ' ml of milk')
print(str(beans) + ' g of coffee beans')
