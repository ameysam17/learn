import sys
import random
from enum import Enum 

def play_rps():

    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3 

    playerschoice = input ("\nEnter ...\n1 for Rock, \n2 for Paper, \n3 for Scissors\n\n") 
    if playerschoice not in ["1", "2", "3"]:
        print("Invalid input. Please enter 1, 2, or 3.")
        return play_rps()  # Restart the game if input is invalid

    player = int(playerschoice)

    computerchoice = random.choice("123")

    computer = int(computerchoice)

    
    print("\nyou chose " + str(RPS(player)).replace("RPS.", "") + ".")
    print("python chose " + str(RPS(computer)).replace("RPS.", "") + ".\n")
    
    if player == 1 and computer == 3:
        print("🥳 you win!")
    elif player == 2 and computer == 1:
        print("🥳 you win!")
    elif player == 3 and computer == 2:
        print("🥳 you win!")
    elif player == computer:
        print("Tie game!😲")
    else:
        print("🐍 python wins!")

    print("\nplay again?")

    while True:
        playagain = input("\nplay again? \nY for yes, \nN for Quit \n\n")
        if playagain.lower() not in ["y", "n"]:
            print("Invalid input. Please enter Y or N.")
            continue
        else:
            break
        if playagain.lower() == "y":
            return play_rps()  # Restart the game if the player wants to play again
        else: 
            print("\nThanks for playing! Goodbye!👋") # It's a logical if Statement 
            print("\n🥳🥳🥳🥳🥳")
            playagain = False
            #break 
            sys.exit("Goodbye!👋")

play_rps()