import random
import time

#Player info
print("Hi there! Welcome to the 'Take Me Out to Dinner' Game!")
print("Let's start with your name, and then get your significant other's name.")
name = ''
sigName = ''
while name == '':
    name = input("What is your name: ")
    name = name.capitalize()
    nameConfirmation = input(f"Your name is {name}, right? (yes/no): ")
    if nameConfirmation.lower() != 'yes':
        name = ''
while sigName == '':
    sigName = input(f"{name}, what is your signicant other's name: ")
    sigName = sigName.capitalize()
    nameConfirmation = input(f"Your significant other's name is {sigName}, right? (yes/no): ")
    if nameConfirmation.lower() != 'yes':
        sigName = ''

#Game Intro
start = False
def intro(name, sigName, start):
    if start:
        pass
    print(f"Welcome {name}! You and {sigName} are going on a date tonight!")
    time.sleep(2)
    print(f"You just have to figure out what type of food {sigName} wants.")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print(f"Oh... and what appetizer {sigName} wants...")
    time.sleep(2)
    print('...')
    time.sleep(.5)
    print(f"And of course, you just have to determine what entree {sigName} wants.")
    time.sleep(2)
    print("\nNo worries... It should be fun! :)")
    print("")

    start = ""
    while start == "":
        start = input("Are you ready to play (yes/no): ")
        if start.lower() == 'yes':
            start = True
        elif start.lower() == 'no':
            start = False
            print("okay, bye bye!")
        else:
            print("I think you mistyped.")
            time.sleep(.5)
            print("Try typing yes or no.")
            start = ""
    return start

def game(name, sigName):
    #all in game options
    cuisineTotalOptions = {'Chinese': {'starter': ['fried rice', 'white rice', 'fried noodles'],
                               'entree': ['dumplings', 'orange chicken', 'beijing beef']},
                   'Italian': {'starter': ['mozzarella sticks', 'salad', 'toasted ravioli'],
                               'entree': ['spaghetti', 'pizza', 'lasagna']},
                   'Mexican': {'starter': ['queso dip', 'guacamole dip', 'nachos'],
                               'entree': ['tacos', 'burrito', 'quesadilla']},
                   'Japanese': {'starter': ['edamame', 'gyoza', 'takoyaki'],
                                'entree': ['miso katsu', 'ramen', 'sushi']}
                           }

    #Types of cuisine spouse / character can choose from.
    cuisineTypeList = []
    for cuisine in cuisineTotalOptions:
        cuisineTypeList.append(cuisine)

    #spouse cuisine choice
    cuisineChoice = cuisineTypeList[random.randint(0, (len(cuisineTypeList) - 1))]

    #player choice / compare to sig choice
    playerChoice = ''
    time.sleep(1)
    print("")
    print(f"{sigName}: Hey, honey, I think we should go out to dinner.")
    time.sleep(1)
    print(f"{sigName}: Should we have {', '.join(cuisineTypeList[0:-1])} or {cuisineTypeList[-1]}.")
    time.sleep(1)
    print('*' * 25)
    print("")
    while playerChoice.lower() != cuisineChoice.lower():
        if len(cuisineTypeList) == 1:
            print(f"I think we should just do {''.join(cuisineTypeList)}")
            playerChoice = cuisineChoice.lower()
        elif len(cuisineTypeList) > 1:
            playerChoice = input(f"{name}: I think we should have (type one of the choices): ")
            print('*' * 25)
            print("")
            if playerChoice.capitalize() not in cuisineTypeList:
                print(f"Your options are {', '.join(cuisineTypeList)}.")

            elif (playerChoice.lower() != cuisineChoice.lower()) and (len(cuisineTypeList) != 1):
                cuisineTypeList.remove(playerChoice.capitalize())
                print(f"{sigName}: How about you choose {' or... '.join(cuisineTypeList)}. I don't feel like {playerChoice.capitalize()}.")
                time.sleep(1.5)
                print('*' * 25)
                print("")
        if playerChoice.lower() == cuisineChoice.lower():
            print(f"{sigName}: I like {playerChoice.capitalize()}. Good Choice!")
            print('*' * 25)
            print("")

    # starter

    time.sleep(1)
    print("\n" * 5)
    print("-" * 10)
    print(f"**AT THE {cuisineChoice.upper()} RESTAURANT**")
    print("-" * 10)
    print("")
    time.sleep(2)
    print(f"Waitress: Hi there! Are you ready to order your meal?")
    print("")
    time.sleep(3)
    print(f"{sigName}: We are! Oh, {name}, I love {cuisineChoice}. Let's get an appetizer!\n")
    time.sleep(3)
    print("Waitress: Your appetizer options are: ")
    for i in range(0, (len(cuisineTotalOptions[cuisineChoice]['starter']))):
        print(str(i + 1) + " " + (cuisineTotalOptions[cuisineChoice]['starter'][i]) + ".")
    time.sleep(2)

    appetizers = []
    for apps in cuisineTotalOptions[cuisineChoice]['starter']:
        appetizers.append(apps)

    app = ""
    sigApp = cuisineTotalOptions[cuisineChoice]['starter'][random.randint(0, 2)]
    while app != sigApp:
        app = input(f"\n{sigName}: Which app should we get: [1] {appetizers[0]}, [2] {appetizers[1]}, [3] {appetizers[2]} (type a number): ")

        if app == '1' or app == '2' or app == '3':
            app = int(app)
            app = cuisineTotalOptions[cuisineChoice]['starter'][app - 1]
            if app != sigApp:
                print(f"{sigName}: I'm not really feeling {app}")

            else:
                print(f"{sigName}: Yes, I definitely want {app}, good choice!")
        else:
            app = ""
            print("You must type a number: 1, 2, or 3.")

# I could have made the starter and entree into a function...
# Consider next time: a nested dictionary can probably use a function, if both keys are called.
    time.sleep(3)
    print("\n" * 5)
    print("-" * 10)
    print(f"**AT THE {cuisineChoice.upper()} RESTAURANT**")
    print("-" * 10)
    print("")
    time.sleep(2)
    print("Waitress: Are you ready for your meal?\n")
    time.sleep(3)
    print(f"{sigName}: Yes, Ma'am! {name}, what meal should we get? \n")
    print("Waitress: Your meal options are: ")
    for i in range(0, (len(cuisineTotalOptions[cuisineChoice]['entree']))):
        print(str(i + 1) + " " + (cuisineTotalOptions[cuisineChoice]['entree'][i]) + ".")
    time.sleep(2)

    entrees = []
    for meals in cuisineTotalOptions[cuisineChoice]['entree']:
        entrees.append(meals)

    meal = ""
    sigMeal = cuisineTotalOptions[cuisineChoice]['entree'][random.randint(0, 2)]
    while meal != sigMeal:
        meal = input(f"{sigName}: Which entree should we get: [1] {entrees[0]}, [2] {entrees[1]}, [3] {entrees[2]} (type a number): ")

        if meal == '1' or meal == '2' or meal == '3':
            meal = int(meal)
            meal = cuisineTotalOptions[cuisineChoice]['entree'][meal - 1]
            if meal != sigMeal:
                print(f"{sigName}: I'm not really feeling {meal}")

            else:
                print(f"{sigName}: Yes, I definitely want {meal}, good choice!")
        else:
            meal = ""
            print("You must type a number: 1, 2, or 3.")

    billOptions = [0, 20.91, 53.37, 121.43, 177.44, 234.98, 500.93, 1000.37]
    bill = billOptions[random.randint(0, (len(billOptions) - 1))]

    print("\n" + ("-" * 25))
    print("1 Romantic Hour Later")
    print(("-" * 25))
    time.sleep(5)
    print("Waitress: Thank you guys for coming tonight!")
    time.sleep(2)
    if bill == 0:
        print("Waitress: A fellow patron decided to pay your bill.")
        print("Waitress: Have a great night!")
    elif bill > 0:
        print(f"Waitress: You can pay your bill of ${bill} at the counter.")
    time.sleep(2)
    print("Waitress: Have a great night!")
    if bill > 150:
        print(f"{name}: ...")
        time.sleep(2)
        print(f"{name} oh...")
        time.sleep(2)
        print(f"{name}: Thanks...")
        time.sleep(2)
        print(f"{name}: You too...")
        time.sleep(2)
        print(f"{name} ***stumbles for wallet***")




start = intro(name, sigName, start)
if start:
    game(name, sigName)