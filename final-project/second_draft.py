#user input
print("Pick your perfect meal deal to find out what type of magical woodland creature you are! 🧝🧚🧙")
score= 0

user_input_main = input("First: Choose your main. Will you have: \na. Sandwich \nb. Sushi \nc. Salad \nAnswer: ")
if user_input_main == "a" or user_input_main == "Sandwich":
    score += 0
    print ("\n")
elif user_input_main == "b" or user_input_main == "Sushi":
    score += 1
    print ("\n") 
elif user_input_main == "c" or user_input_main == "Salad":
    score += 2
    print ("\n") 
else:
     print ("Incorrect input, please choose a, b, or c")
     print ("\n")

user_input_snack = input("Second: Choose a snack. Do you fancy: \na. Crisps \nb. Chocolate \nc. Fruit \nAnswer: ")
if user_input_snack == "a" or user_input_snack == "Crisps":
    score += 0
    print ("\n")
elif user_input_snack == "b" or user_input_snack == "Chocolate":
    score += 1
    print ("\n") 
elif user_input_snack == "c" or user_input_snack == "Fruit":
    score += 2
    print ("\n") 
else:
     print ("Incorrect input, please choose a, b, or c")
     print ("\n")

user_input_drink = input("Third: Choose a drink. Will you wash it down with: \na. Pop \nb. Smoothie \nc. Coffee \nAnswer: ")
if user_input_drink == "a" or user_input_drink == "Pop":
    score += 0
    print ("\n")
elif user_input_drink == "b" or user_input_drink == "Smoothie":
    score += 1
    print ("\n") 
elif user_input_drink == "c" or user_input_drink == "Coffee":
    score += 2
    print ("\n") 
else:
     print ("Incorrect input, please choose a, b, or c")
     print ("\n")

#score
if score <= 2:
        print ("Troll: Here for a heartiest meal you can get for £3.50 🧙🍄👣")
elif score == 3 or 4:
         print ("Fairy: You're picky and take a long time over your choices. Nothing but the best for you. 🧚✨🍀")
elif score >= 5:
    print ("Elf: you are shrewd and pratical in your selection. Substance over style. 🧝🌱🌜")
   
    