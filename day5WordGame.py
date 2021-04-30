import random
import string
#variables
wordList = ["aardvark", "buzzsaw", "concoction", "department", "elevator", "felicity", "gorgeous"]
chosenWord = wordList[random.randint(0, (len(wordList) - 1))]
wrongGuess = 0
checker = list(chosenWord)
dashes = list(len(chosenWord) * "-")
guesses = []
num = string.digits

#Game Logic

print("Let's play a word game!")
print("You have to guess a word letter by letter.")
print("Three incorrect guesses, and it's game over!")
print("Let's begin!")

while checker != []:
    guess = input("type a letter: ")
    if guess in guesses:
        print("You guessed that letter already! :)")
    if guess in num:
        print("There's no numbers in these words")
    else:
        if guess not in num:
            guesses.append(guess)
        if len(guess) == 1:
            if [i for i in guess if i in chosenWord]:
                print(f"{guess} is in the word!")
                for position in range(len(chosenWord)):
                    if guess == chosenWord[position - 1]:
                        dashes[position - 1] = guess
                while guess in checker:
                    checker.remove(guess)
                print("The word so far: " + ''.join(dashes))
                print(f"Letter's guessed: {', '.join(guesses)}")

            else:
                print(f"{guess} is not in the word!")
                print(f"Letter's Guessed: {', '.join(guesses)}")
                wrongGuess = (wrongGuess + 1)
                print(f"Number of wrong guesses = {wrongGuess}.")



    if wrongGuess == 3:
        print("You lose!")
        print(f"The word was: {chosenWord}.")
        exit()

print("Winner!")
