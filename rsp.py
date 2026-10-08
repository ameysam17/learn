import sys
import random
from enum import Enum 

def rps():
    print("\nWelcome to Rock, Paper, Scissors! 🪨📄✂️\n")
    print("Instructions:")
    print("1. Choose your move by entering the corresponding number.")
    print("2. The computer will randomly select its move.")
    print("3. The winner will be determined based on the classic rules of Rock, Paper, Scissors.\n")
    print("Let's play!\n")
    game_count = 0
    player_wins = 0
    python_wins = 0


    def play_rps():
        nonlocal player_wins, python_wins

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

        nonlocal game_count
        game_count += 1
        print("\nGame count: " + str(game_count))
        print("\nPlayer wins: " + str(player_wins))
        print("\nPython wins: " + str(python_wins))

        print("\nplay again?")

        while True:
            playagain = input("\nplay again? \nY for yes, \nN for Quit \n\n")

            def decide_winner(player, computer):
                nonlocal player_wins, python_wins
                if player == computer:
                    return "Tie game!😲"
                elif (player == 1 and computer == 3) or (player == 2 and computer == 1) or (player == 3 and computer == 2):
                    player_wins += 1
                    return "🥳 you win!"
                else:
                    python_wins += 1
                    return "🐍 python wins!"

            game_result = decide_winner(player, computer)

            print(game_result)

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

    return play_rps()            

play = rps()
