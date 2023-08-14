import random
def RockPaperScissors():
    # list of options
    gameOptions= ['R', 'P', 'S']
    computerScore= 0
    userScore= 0
    while True:
        userChoice= input("Your turn(R/P/S) or 'E/e' to Exit: ")
        if userChoice == 'E' or userChoice == 'e':
            break
        elif userChoice not in gameOptions:
            print("Invalid Input. Please input from the given options.")
            continue
        computerChoice= random.choice(gameOptions)
        # displaying both moves
        print("You chose: ", userChoice)
        print("Computer chose:", computerChoice)
        # handling win and draw conditions
        if userChoice == computerChoice:
            print("DRAW!")
        elif userChoice == 'S' and computerChoice == 'R':
            print("COMPUTER WINS!")
            computerScore+= 1
        elif userChoice == 'P' and computerChoice == 'S':
            print("COMPUTER WINS!")
            computerScore+= 1
        elif userChoice == 'R' and computerChoice == 'P':
            print("COMPUTER WINS!")
            computerScore+= 1
        else:
            print("YOU WIN!")
            userScore+= 1
    # printing scores
    print("Your Score: ", userScore)
    print("Computer Score: ", computerScore)
def main():
    print("Rock Paper Scissors\n-------------------")
    print("Rules:\n1. Rock beats Scissors\n2. Scissors beat Paper\n3. Paper beats Rock\n")
    while True:
        RockPaperScissors()
        reMatch= input("Do you want a rematch? (Y/N): ")
        if reMatch.lower() != 'y':
            print("Goodbye :)")
            break
if __name__ == "__main__":
    main()