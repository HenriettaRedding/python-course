#1a
price = float(input("what is the price of the shirt?"))
colour = (input("what is the colour of the shirt?"))

answer = (price <= 25.00) and (colour == "yellow")

print(f"shirt is avalible within budget and correct colour: {answer}")