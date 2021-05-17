# To use, create a guests.txt file with all of your guests separated by commas.
# create a file called 'letterToGuests.txt' and write your letter in this file.
    #Anywhere that you want a name replaced, write (name)

def nameChange():
    with open('guests.txt') as guests:
        names = guests.read()
        guestList = names.split(", ")
        print(guestList)
    with open('letterToGuests.txt') as letter:
        contents = letter.read()
        for i in range(0, (len(guestList))):
            name = guestList[i]
            firstnameList = str.split(name)
            firstname = firstnameList[0]
            new = contents.replace('(name)', firstname)
            print(new)
            print('\n')
            with open(f"{name}'sletter.txt", mode="w") as newLetter:
                newLetter.write(new)
nameChange()

###Add giftChange function or other similar function for Krista and Jacob's wedding.###

### practice ### ignore
# with open('myFile.txt') as file:
#     contents = file.read()
#     print(contents)
#
# with open('newFile.txt', mode='w') as file:
#     file.write("\nI am the sexiest, baddest, mofo of them all.")
#
# with open('newFile.txt') as file:
#     contents = file.read()
#     print(contents)

# score = 0
# with open('../../../Desktop/myFile.txt') as myFile:
#     highScore = myFile.read()
#     print(highScore)
#
# num = input("number: ")
#
# newHighScore = num
#
# with open('/Users/setan/Desktop/myFile.txt', mode='w') as myFile:
#     myFile.write(newHighScore)
