import sys
import random
from enum import Enum 

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3 

playagain = True

while playagain:
   
    playerschoice = input ("\nEnter ...\n1 for Rock, \n2 for Paper, \n3 for Scissors\n\n") 

    player = int(playerschoice)

    if player < 1 or player > 3:
        sys.exit(" you must enter a number between 1,2,3.")

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

    playagain = input("\nplay again? \nY for yes, \nN for Quit \n\n")

    if playagain.lower() == "y":
        playagain = True
    else: 
        print("\nThanks for playing! Goodbye!👋")
        print("\n🥳🥳🥳🥳🥳")
        playagain = False
        #break 

    sys.exit("Goodbye!👋")    