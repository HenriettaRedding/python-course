#Replicating a trashy buzzfeed type quiz
def user_input_main():
    choices= ["Sandwich", "Sushi", "Salad"]
    user_input_snack
    choice = ["Crisps", "Chocolate", "Fruit"]
    incorrect_user_input
#user input
print("Pick your perfect meal deal to find out what type of woodland creature you are:")
user_input_main = input("First: Choose your main. Will you have: Sandwich, Sushi or Salad?")
user_input_snack = input ("Second: Choose a snack. Do you fancy Crisps, Chocolate or Fruit?")
user_input_drink = input ("Third: Choose a drink. Will you wash it down with Pop, Smoothie, or Coffee?")

try:
         while incorrect_user_input:
            rock_paper_scissors = input("Choose either Rock, Paper of Scissors: [R/P/S] ")
            if rock_paper_scissors.upper().startswith ("R"):
                incorrect_user_input= False
                move = 0
            elif rock_paper_scissors.upper().startswith ("P"):
                incorrect_user_input = False
                move = 1   
            elif rock_paper_scissors.upper().startswith ("S"):
                incorrect_user_input = False
                move = 2
            else:
                print("Incorrect input!")
            if not incorrect_user_input:
                print (f"Choice: {move}")
                return move
    except:
        return False
