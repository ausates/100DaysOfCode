import random
import time

thingsToDoToday = {}

numberOfThingsToDo = input("Number of optimized things I want to do today: ")
try:
    numberOfThingsToDo = int(numberOfThingsToDo)
    if isinstance(numberOfThingsToDo, int):
        for i in range(1, (numberOfThingsToDo + 1)):
            thingsToDoToday[i] = ""
        for thing in range(1, (numberOfThingsToDo + 1)):
            thingsToDoToday[thing] = input(f"My number {thing} thing to do: ")

except:
    print("Austin... this is an app you made... how you gonna fuck it up?")
    exit()

timeToSpend = {}
for items in range(1, (len(thingsToDoToday) + 1)):
    timeCount = input(f"In MINUTES, how long do you want to spend on ({thingsToDoToday[items]}): ")
    timeToSpend[items] = timeCount

print(timeToSpend)

def timer(timeToSpend):
    try:
        timeToSpend = int(timeToSpend)
        if isinstance(timeToSpend, int):
            #This allows me to display minutes, and then countdown in seconds for the last minutes.
            for i in range(0, timeToSpend):
                minutesLeft = (timeToSpend - i)
                if minutesLeft > 1:
                    print(f"There are {minutesLeft} minutes left.")
                    time.sleep(60)
                elif minutesLeft == 1:
                    for i in range(0, 60):
                        minutesLeft = (60 - i)
                        time.sleep(1)
                        print(minutesLeft)
    except:
        print("fail")

thingsToDoBetweenSets = ['Text Lexi that you love her.', 'clean something', 'add to your coding projects', 'do something with the dogs']
for x in thingsToDoToday:
    timer(timeToSpend[x])
    print(x)
    finished = input("Do you want to take a quick break? (yes/no): ")
    if finished.lower() == 'yes':
        print("Take a five minute break and:")
        print(thingsToDoBetweenSets[random.randint(0, (len(thingsToDoBetweenSets) - 1))])
        breakTime = 5
        for i in range(0, breakTime):
            print(f"{breakTime - i} minutes remaining.")
            time.sleep(60)




