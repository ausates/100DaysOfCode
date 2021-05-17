import time
import random

print("Welcome to the Band Name Generator!")
time.sleep(.5)
bandName = ""
personalName = input("What is your name: ")
city = input("What city were you born in: ")
adList = ["too", "happy", "big", "little", "zealous"]
adjective = adList[random.randint(0, (len(adList) - 1))]
petTest = input("Do you have a pet (yes/no): ")
if petTest.lower() == "yes":
    pet = input("What is your pet's name: ")
    petType = input("What kind of animal is your pet: ")
else:
    pet = 0
    petType = 0
genre = input("What genre does your band play: ")

if pet == 0 and petType == 0:
    bandNameList = [adjective, genre, personalName, city]
    while bandName == "":
        bandNamePartOne = bandNameList[random.randint(0, 3)]
        bandNamePartTwo = bandNameList[random.randint(0, 3)]
        bandName = (bandNamePartOne + " " + bandNamePartTwo)
        print("You cold try: " + bandName.upper())
        bandNamePartOne = bandNameList[random.randint(0, 3)]
        bandNamePartTwo = bandNameList[random.randint(0, 3)]
        bandName = (bandNamePartOne + " " + bandNamePartTwo)
        print("or: " + bandName.upper())
        bandName = (adList[random.randint(0, (len(adList) - 1))] + " " + bandNameList[random.randint(0, 3)])
        print("or: " + bandName.upper())
        bandName = (adList[random.randint(0, (len(adList) - 1))] + " " + bandNameList[random.randint(0, 3)])
        print("or :" + bandName.upper())
else:
    bandNameList = [adjective, personalName, city, genre, pet, petType]
    while bandName == "":
        bandNamePartOne = bandNameList[random.randint(0, (len(bandNameList)-1))]
        bandNamePartTwo = bandNameList[random.randint(0, (len(bandNameList)-1))]
        bandName = (bandNamePartOne + " " + bandNamePartTwo)
        print("You cold try: " + bandName.upper())
        bandNamePartOne = bandNameList[random.randint(0, (len(bandNameList)-1))]
        bandNamePartTwo = bandNameList[random.randint(0, (len(bandNameList)-1))]
        bandName = (bandNamePartOne + " " + bandNamePartTwo)
        print("or: " + bandName.upper())
        bandName = (adList[random.randint(0, (len(adList) - 1))] + " " + bandNameList[random.randint(0, (len(bandNameList)-1))])
        print("or: " + bandName.upper())
        bandName = (adList[random.randint(0, (len(adList) - 1))] + " " + bandNameList[random.randint(0, (len(bandNameList)-1))])
        print("or :" + bandName.upper())
