#ROCK PAPER SCISSORS
#user input
def rock_paper_sicissors():
    choices= ["R", "P", "S"]
    incorrect_user_input = True
    move= -1

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

#computer input
def computer_choice():
    from random import randint
    return randint(0,2)

#logic
def logic(user, computer):
    score_matrix = {
        #first value user, second value computer
        0: {0: 0 ,1:-1 ,2: 1 },
        1: {0: 1 ,1: 0 ,2:-1 },
        2: {0:-1 ,1: 1 ,2: 0 }
    }
    state = score_matrix[user][computer]
    return state

#score
def main ():
    score= 0
    game = 2

    for game_number in range(3):
        user= rock_paper_sicissors()
        ai = computer_choice()
        score= score + logic (user, ai)
        #print (user, ai, score)

        #result
        print ()
        if score == 0:
          win_draw_lose = "Draw"
        elif score == -1:
           win_draw_lose = "Lose"
        elif score == 1:
            win_draw_lose = "Win"
        print (F"Game number #{game_number} Current score is: {score}")

        print()
        choice = ["Rock", "Paper", "Scissors"]

        print(f"{choice[user]} vs {choice[ai]} - {win_draw_lose}")
        print ("-"*41)
        print ("-="*20+"-")

        print ()
        if score > 0:
            print (f"You Win!")
        elif score < 0:
            print (f"You Lose!")
        else:
         print (f"You Drew!")
main()


