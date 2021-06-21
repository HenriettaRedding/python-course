#2a&2b
shopping_cost = int(input("What is the total price of your shopping? "))
discount_applicable = (input("Do you have a discount code? y/n "))
if (shopping_cost > 20):
    total_cost = shopping_cost * 0.9
elif (shopping_cost >= 100):
    total_cost = shopping_cost * 0.05
else:
    total_cost = shopping_cost
print(f'This total cost is {total_cost}')