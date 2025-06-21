from random import randint
easy_number_turns = 10
hard_number_turns = 5

def difficulty_level():
    level = input("choose the level of difficulty.Type 'easy' or 'hard' ")
    if level == "easy":
        return easy_number_turns
    else:
        return hard_number_turns
  

def number_guessing(answer,number_input,turns):
    if answer < number_input:
        print("you are too high")
        return turns-1
    elif answer > number_input:
        print("you are too low")
        return turns-1
    else:
        print(f"you got it the number is {number_input}")
        return -1

def game():
    print("welcome to Number guessing game!")
    print(r""" __  ___           __                ______                              
    /  |/  /___ ______/ /_____  _____   / ____/___  ____ ___  ____ _____  ___ 
/  /|_/ / __ `/ ___/ __/ __ \/ ___/  / / __/ __ \/ __ `__ \/ __ `/ __ \/ _ \
 / /  / / /_/ (__  ) /_/ /_/ / /     / /_/ / /_/ / / / / / / /_/ / /_/ /  __/
/_/  /_/\__,_/____/\__/\____/_/      \____/\____/_/ /_/ /_/\__,_/ .___/\___/ 
                                                                /_/          
""")
    answer = randint(1,100)

    turns = difficulty_level()

    
    while turns > 0:
        print(f"\nYou have {turns} turn(s) left.")
        number = int(input("Enter a number: "))
        turns = number_guessing(answer, number, turns)

        if turns == -1:
            break  # Correct guess, exit the game
        elif turns == 0:
            print("You're out of attempts! You lose.")
        else:
            print("Guess again.")

game()

