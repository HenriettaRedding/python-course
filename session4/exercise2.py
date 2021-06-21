#2a
def shopping_calculator(shopping_cost):
    if shopping_cost < 20:
        return shopping_cost
    else:
        return shopping_cost * 0.9
y= shopping_calculator(30.5)
print(f"The total cost is: £{y}")