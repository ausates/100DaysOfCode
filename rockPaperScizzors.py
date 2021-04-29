import random
import time

def quitGame():
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    print("bye bye")
    exit()

def playGame():

    winner = False
    loser = False

    while winner == loser:
        roundOne = 0
        roundTwo = 0
        roundThree = 0

        options = ["rock", "paper", "scissors"]
        numOptions = [1, 2, 3]

        while roundOne == 0:
            print("Round One!!")
            print("In a moment, you will choose either rock, paper, or scissors with **A NUMBER**")
            time.sleep(1)
            playerChoice = input("Please choose rock[1], paper[2], scissors[3]: ")
            try:
                playerChoice = int(playerChoice)
                if playerChoice in numOptions:
                    playerChoice = options[(playerChoice - 1)]
            except:
                print("You must have put in a bad input. Let's try this round again!")

            opponentChoice = options[random.randint(0, 2)]

            if playerChoice == opponentChoice:
                print(f"You both had {playerChoice}!")
                print("Let's try this round again!")
                roundOne = 0
            else:
                print(f"You chose {playerChoice}, and your opponent chose {opponentChoice}.")
                if (playerChoice == "rock") and (opponentChoice == "scissors"):
                    print("win")
                    roundOne = 1
                elif (playerChoice == "scissors") and (opponentChoice == "paper"):
                    print("win")
                    roundOne = 1
                elif (playerChoice == "paper") and (opponentChoice == "rock"):
                    print("win")
                    roundOne = 1
                else:
                    print("lose")
                    roundOne = 2


        while roundTwo == 0:
            print("Round Two!!")
            print("In a moment, you will choose either rock, paper, or scissors with **A NUMBER**")
            time.sleep(1)
            playerChoice = input("Please choose rock[1], paper[2], scissors[3]: ")
            try:
                playerChoice = int(playerChoice)
                if playerChoice in numOptions:
                    playerChoice = options[(playerChoice - 1)]
            except:
                print("You must have put in a bad input. Let's try this round again!")

            opponentChoice = options[random.randint(0, 2)]

            if playerChoice == opponentChoice:
                print(f"You both had {playerChoice}!")
                print("Let's try this round again!")
                roundTwo = 0
            else:
                print(f"You chose {playerChoice}, and your opponent chose {opponentChoice}.")
                if (playerChoice == "rock") and (opponentChoice == "scissors"):
                    print("win")
                    roundTwo = 1
                elif (playerChoice == "scissors") and (opponentChoice == "paper"):
                    print("win")
                    roundTwo = 1
                elif (playerChoice == "paper") and (opponentChoice == "rock"):
                    print("win")
                    roundTwo = 1
                else:
                    print("lose")
                    roundTwo = 2

        if roundOne == roundTwo:
            roundThree = roundOne

        while roundThree == 0:
            print("Round Three!!")
            print("In a moment, you will choose either rock, paper, or scissors with **A NUMBER**")
            time.sleep(1)
            playerChoice = input("Please choose rock[1], paper[2], scissors[3]: ")
            try:
                playerChoice = int(playerChoice)
                if playerChoice in numOptions:
                    playerChoice = options[(playerChoice - 1)]
            except:
                print("You must have put in a bad input. Let's try this round again!")

            opponentChoice = options[random.randint(0, 2)]

            if playerChoice == opponentChoice:
                print(f"You both had {playerChoice}!")
                print("Let's try this round again!")
                roundThree = 0
            else:
                print(f"You chose {playerChoice}, and your opponent chose {opponentChoice}.")
                if (playerChoice == "rock") and (opponentChoice == "scissors"):
                    print("win")
                    roundThree = 1
                elif (playerChoice == "scissors") and (opponentChoice == "paper"):
                    print("win")
                    roundThree = 1
                elif (playerChoice == "paper") and (opponentChoice == "rock"):
                    print("win")
                    roundThree = 1
                else:
                    print("lose")
                    roundThree = 2

        if (roundOne == 1 and roundTwo == 1) or (roundOne == 1 and roundThree == 1) or (roundTwo == 1 and roundThree == 1):
            winner = True
            print("You're the winner!")
            time.sleep(1)
        elif (roundOne == 2 and roundTwo == 2) or (roundOne == 2 and roundThree == 2) or (roundTwo == 2 and roundThree == 2):
            loser = True
            print("Sorry, you lost.")


    print("")
    startGame = False

print("Let's play rock, paper, scissors!")
time.sleep(.5)

startGame = False

rpsrules = ""
while rpsrules == "":
    rpsrules = input("Do you know how to play (yes/no): ")
    if rpsrules.lower() == "yes":
        wannaPlay = input("Would you like to play (yes/no): ")
        if wannaPlay.lower() == "yes":
            startGame = True
        elif wannaPlay.lower() == "no":
            print("Okay...")
            quitGame()
        else:
            print("seems you mistyped...")
            print("Let the games begin, anyway!")
            startGame = True
    elif rpsrules.lower() == "no":
        print("In rock, paper, scissors you and your opponent want to win each round.")
        time.sleep(2.5)
        print("Each round you will choose one of three choices: rock, paper, or scissors.")
        time.sleep(2.5)
        print("In rock, paper, scissors: rock > scissors; paper > rock; scissors > paper.")
        time.sleep(2.5)
        print("Your goal is to win at least 2 of 3 rounds.")
        time.sleep(5)
        print("Let's begin!")
        startGame = True
        time.sleep(.5)
    else:
        print("You mistyped.")
        rpsrules = ""

while startGame:
    playGame()
    startGame = False

print("Thanks for playing!")