#user input
print ("\n")
print("🧝 ~Pick your perfect meal deal to find out what type of magical woodland creature you are!~ 🧚")
score= 0
print ("\n")

user_input_main = input("First: Choose your main. Will you have: \na. Sandwich \nb. Sushi \nc. Salad \nd. Wrap \nAnswer: ")
if user_input_main == "a" or user_input_main == "Sandwich":
    score += 0
    print ("\n")
elif user_input_main == "b" or user_input_main == "Sushi":
    score += 1
    print ("\n") 
elif user_input_main == "c" or user_input_main == "Salad":
    score += 2
    print ("\n") 
elif user_input_main == "d" or user_input_main == "Wrap":
    score += 3
    print ("\n") 
else:
     print ("Incorrect input, please choose a, b, c, or d")
     print ("\n")

user_input_snack = input("Second: Choose a snack. Do you fancy: \na. Crisps \nb. Chocolate \nc. Fruit \nd. Popcorn \nAnswer: ")
if user_input_snack == "a" or user_input_snack == "Crisps":
    score += 0
    print ("\n")
elif user_input_snack == "b" or user_input_snack == "Chocolate":
    score += 1
    print ("\n") 
elif user_input_snack == "c" or user_input_snack == "Fruit":
    score += 2
    print ("\n") 
elif user_input_snack == "d" or user_input_snack == "Popcorn":
    score += 3
    print ("\n") 
else:
     print ("\n")
     print ("!Incorrect input, please choose a, b, or c!")
     print ("\n")

user_input_drink = input("Third: Choose a drink. Will you wash it down with: \na. Pop \nb. Smoothie \nc. Coffee \nd. Energy Drink \nAnswer: ")
if user_input_drink == "a" or user_input_drink == "Pop":
    score += 0
    print ("\n")
elif user_input_drink == "b" or user_input_drink == "Smoothie":
    score += 1
    print ("\n") 
elif user_input_drink == "c" or user_input_drink == "Coffee":
    score += 2
    print ("\n") 
elif user_input_drink == "d" or user_input_drink == "Energy Drink":
    score += 3
    print ("\n") 
else:
    print ("\n")
    print ("!Incorrect input, please choose a, b, c or d!")
    print ("\n")

#score
if score <= 2:
        print ("Troll: Here for a heartiest meal you can get for £3.50 🧙🍄👣")
elif score == 3:
        print ("Fairy: You're picky and take a long time over your choices. Nothing but the best for you. 🧚✨🍀")
elif score == 4:
        print ("Fairy: You're picky and take a long time over your choices. Nothing but the best for you. 🧚✨🍀")
elif score ==5:
        print ("Sorcerer: Your choices are chaotic and malevolent- no one should get on your bad said untill you finish eating. 🧞🔮☁️")
elif score == 6:
    print ("Elf: you are shrewd and pratical in your selection. Substance over style. 🧝🌱🌜")
elif score == 7:
    print ("Elf: you are shrewd and pratical in your selection. Substance over style. 🧝🌱🌜")
elif score >= 8:
    print("Unicorn: Is it even worth eating if it hasnt got a little bit of *sparkle*? 🦄💫🌈")