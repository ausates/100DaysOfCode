import random
import time


start = False
def startGame(start):
    while start != True:
        start = input("Do you know how to play Black Jack (yes/no): ")
        if start.lower() == "no":
            print("Your goal is to score 21, or have a score higher than the dealer.")
            time.sleep(2.5)
            print("To start, you will be dealt 2 cards, and the dealer will be dealt two cards.")
            time.sleep(2.5)
            print("You will see your two cards, but only ONE of the dealer's cards.")
            time.sleep(2.5)
            print("Based on your cards, you have to decide whether to take another card.")
            print("-" * 15)
            time.sleep(3)
            print("If you take another card, but go over 21, you 'bust' and lose.")
            time.sleep(2.5)
            print("If you take a card and reach exactly 21, the dealer will draw until they bust or also get 21.")
            time.sleep(2.5)
            print("if you take a card and don't reach 21, you may draw again or stay with your current set.")
            time.sleep(2.5)
            start = input("Are you ready to play (yes/no): ")
            if start.lower() == "no":
                print("Okay, bye, then!")
                exit()
            elif start.lower() == "yes":
                start = True
            else:
                print("Bad Input: type 'yes' or 'no'.")
        elif start.lower() == "yes":
            start = True
        else:
            print("Bad Input: type 'yes' or 'no'.")

    return start


def game(start):
    def replay():
        start = input("Would you like to play again: ")
        if start.lower() == "yes":
            start = True
        elif start.lower() == "no":
            start = False
            exit()
        else:
            print("You mistyped. Goodbye.")
            start = False
            exit()
        return start
    playerHand = {'card 1': 0, 'card 2': 0}
    dealerHand = {'card 1': 0, 'card 2': 0}
    possibleCards = ['A', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    cardValues = {'A': 11, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10}
    print("\n" * 5)
    print("-" * 15)
    ## Round One
    for card in playerHand:
        playerHand[card] = possibleCards[random.randint(0, (len(possibleCards) - 1))]
    for card in dealerHand:
        dealerHand[card] = possibleCards[random.randint(0, (len(possibleCards) - 1))]
#Player's Cards
    pcard1 = playerHand['card 1']
    pcard2 = playerHand['card 2']
#Player cards individual values
    valpcard1 = cardValues[pcard1]
    valpcard2 = cardValues[pcard2]
#Player Cards total values
    playerCardValue = (valpcard1 + valpcard2)
#Dealer Cards
    dcard1 = dealerHand['card 1']
    dcard2 = dealerHand['card 2']
#Dealer Card Individual Values
    valdcard1 = cardValues[dcard1]
    valdcard2 = cardValues[dcard2]
#Dealer Cards total values
    dealerCardValues = (valdcard1 + valdcard2)
    if playerCardValue == 21:
        print("Black Jack!")
        print(f"Your cards are: {pcard1}, {pcard2}.")
        print("!" * 25)
        replay()
    elif playerCardValue < 21:
        print(f"Your cards: {pcard1}, {pcard2}. \n")
        print(f"Dealer's showing card: {dcard1}. \n")
        time.sleep(1)
        print(f"Your total card value is: {playerCardValue}")
    if playerCardValue < 21:
        hit = ""
        while hit == "":
            print("You can hit (add an extra card) or stay (keep your current cards).")
            hit = input("Would you like to 'hit' or 'stay' (hit/stay): ")
            if hit.lower() == "hit":
                playerHand['card 3'] = possibleCards[random.randint(0, (len(possibleCards) - 1))]
                print(f"you drew a {playerHand['card 3']}.")
                pcard3 = playerHand['card 3']
                valpcard3 = cardValues[pcard3]
                playerCardValue = (playerCardValue + valpcard3)
                print(f"Your total card value is: {playerCardValue}")
                if (playerCardValue > 21) and (pcard1 == 'A'):
                    print("You have an ace in your hand, let's make one low")
                    pcard1 = '1'
                    playerCardValue = (playerCardValue - 10)
                    print(f"Your total card value is {playerCardValue}.")

                elif (playerCardValue > 21) and (pcard2 == 'A'):
                    print("You have an ace in your hand, let's make one low")
                    pcard2 = '1'
                    playerCardValue = (playerCardValue - 10)
                    print(f"Your total card value is {playerCardValue}.")

                elif (playerCardValue > 21) and (pcard3 == 'A'):
                    print("You have an ace in your hand, let's make one low")
                    pcard3 = '1'
                    playerCardValue = (playerCardValue - 10)
                    print(f"Your total card value is {playerCardValue}.")
#draw 4
                if (playerCardValue < 21) and (hit.lower() == "hit"):
                    hit = ""
                    while hit == "":
                        hit = input("Would you like to 'hit' or 'stay' (hit/stay): ")
                        if hit.lower() == "hit":
                            playerHand['card 4'] = possibleCards[random.randint(0, (len(possibleCards) - 1))]
                            print(f"You drew a {playerHand['card 4']}.")
                            pcard4 = playerHand['card 4']
                            valpcard4 = cardValues[pcard4]
                            playerCardValue = (playerCardValue + valpcard4)
                            print(f"Your total card value is: {playerCardValue}")
#Test for Ace on bust and converting so it isn't lowered again on second bust
                            if (playerCardValue > 21) and (pcard1 == 'A'):
                                print("You have an ace in your hand, let's make one low")
                                pcard1 = '1'
                                playerCardValue = (playerCardValue - 10)
                                print(f"Your total card value is {playerCardValue}.")
                            elif (playerCardValue > 21) and (pcard2 == 'A'):
                                print("You have an ace in your hand, let's make one low")
                                pcard2 = '1'
                                playerCardValue = (playerCardValue - 10)
                                print(f"Your total card value is {playerCardValue}.")
                            elif (playerCardValue > 21) and (pcard3 == 'A'):
                                print("You have an ace in your hand, let's make one low")
                                pcard3 = '1'
                                playerCardValue = (playerCardValue - 10)
                                print(f"Your total card value is {playerCardValue}.")
                            elif (playerCardValue > 21) and (pcard4 == 'A'):
                                print("You have an ace in your hand, let's make one low")
                                pcard4 = '1'
                                playerCardValue = (playerCardValue - 10)
                                print(f"Your total card value is {playerCardValue}.")
#Draw 5
                    if playerCardValue < 21 and (hit.lower() == "hit"):
                        hit = ""
                        while hit == "":
                            hit = input("Would you like to 'hit' or 'stay' (hit/stay): ")
                            if hit.lower() == "hit":
                                playerHand['card 5'] = possibleCards[random.randint(0, (len(possibleCards) - 1))]
                                print(f"You drew a {playerHand['card 5']}.")
                                pcard5 = playerHand['card 5']
                                valpcard5 = cardValues[pcard5]
                                playerCardValue = (playerCardValue + valpcard5)
                                print(f"Your total card value is: {playerCardValue}")
                                # Test for under 21 ... win
                                if playerCardValue < 21:
                                    print("Wow! 5 cards without a bust! You win!!!!!")
                                    replay()
# Test for Ace on bust
                                if (playerCardValue > 21) and (pcard1 == 'A'):
                                    print("You have an ace in your hand, let's make one low")
                                    pcard1 = '1'
                                    playerCardValue = (playerCardValue - 10)
                                    print(f"Your total card value is {playerCardValue}.")
                                elif (playerCardValue > 21) and (pcard2 == 'A'):
                                    print("You have an ace in your hand, let's make one low")
                                    pcard2 = '1'
                                    playerCardValue = (playerCardValue - 10)
                                    print(f"Your total card value is {playerCardValue}.")
                                elif (playerCardValue > 21) and (pcard3 == 'A'):
                                    print("You have an ace in your hand, let's make one low")
                                    pcard3 = '1'
                                    playerCardValue = (playerCardValue - 10)
                                    print(f"Your total card value is {playerCardValue}.")
                                elif (playerCardValue > 21) and (pcard4 == 'A'):
                                    print("You have an ace in your hand, let's make one low")
                                    pcard4 = '1'
                                    playerCardValue = (playerCardValue - 10)
                                    print(f"Your total card value is {playerCardValue}.")
                                elif (playerCardValue > 21) and (pcard5 == 'A'):
                                    print("You have an ace in your hand, let's make one low")
                                    pcard5 = '1'
                                    playerCardValue = (playerCardValue - 10)
                                    print(f"Your total card value is {playerCardValue}.")

            elif hit.lower() == "stay":
                print("stay it is!")
                pass
            else:
                print("You must type 'hit' or 'stay'.")
                hit = ""
#Test Bust
    if playerCardValue > 21:
        print("You busted! You lose.")
        replay()
#Test 21 even
    if playerCardValue == 21:
        print("Nice!!! You're at 21!")
#Time and space delay for UI
    time.sleep(1)
    print("\n")
#Dealer Turn
    print(f"Dealer's cards are: {dcard1} and {dcard2}")
    time.sleep(.7)
    while (dealerCardValues < playerCardValue) and (dealerCardValues < 21):
        print("Dealer draws")
        time.sleep(1)
        dealerHand['card 3'] = possibleCards[random.randint(0, (len(possibleCards) - 1))]
        dcard3 = dealerHand['card 3']
        valdcard3 = cardValues[dcard3]
        dealerCardValues = (dealerCardValues + valdcard3)
        print(f"Dealer's cards are: {dcard1}, {dcard2} and {dcard3}")
        if (dealerCardValues < playerCardValue) and (dealerCardValues < 21):
            print("Dealer draws")
            time.sleep(1)
            dealerHand['card 4'] = possibleCards[random.randint(0, (len(possibleCards) - 1))]
            dcard4 = dealerHand['card 4']
            valdcard4 = cardValues[dcard4]
            dealerCardValues = (dealerCardValues + valdcard4)
            print(f"Dealer's cards are: {dcard1}, {dcard2}, {dcard3}, and {dcard4}")
            if (dealerCardValues < playerCardValue) and (dealerCardValues < 21):
                print("Dealer draws")
                time.sleep(1)
                dealerHand['card 5'] = possibleCards[random.randint(0, (len(possibleCards) - 1))]
                dcard5 = dealerHand['card 5']
                valdcard5 = cardValues[dcard5]
                dealerCardValues = (dealerCardValues + valdcard5)
                print(f"Dealer's cards are: {dcard1}, {dcard2}, {dcard3}, {dcard4}, and {dcard5}")

# Win logic
    if dealerCardValues > 21:
        print("Dealer Busted!")
        print("You're a winner!")
    elif (dealerCardValues < playerCardValue):
        print("You're a winner!")
    elif playerCardValue < dealerCardValues:
        print("You lose!")
    elif playerCardValue == dealerCardValues:
        print("Tie!")
    else:
        print("Something went grievously wrong... blame the programmer.")

    replay()


start = startGame(start)
print("Let's Play Some Black Jack!")
time.sleep(1.5)
while start:
    start = game(start)

print("Thanks for playing!")