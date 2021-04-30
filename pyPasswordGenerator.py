import random
import string

print("Let's build a new password!")

#importing the ascii character...
# if variable holds method in list, the method will be called, but the list will only have 1 element, technically... weird
alphabet = string.ascii_lowercase + string.ascii_uppercase
num = string.digits
prints = string.printable

#making symbols because the string call doesn't have just symbols for some reason.
# decided to hardcode symbols because of the /n and other odd symbols...

# syma = [i for i in prints if i not in alphabet]
# symbols = [i for i in syma if i not in num]
symbols = ['!','$','%','&','*','+','-','~', '@', '=']

#character requirements code.
alpha = ""
while alpha == "":
    alpha = input("How many LETTERS do you want in your password (minimum of 2): ")
    try:
        alpha = int(alpha)
        if isinstance(alpha, int):
            if alpha < 2:
                print("Sorry, you must have at least 2 letters")
                alpha = ""
    except:
        print("You must type a number.")

numba = ""
while numba == "":
    numba = input("How many NUMBERS do you want in your password: ")
    try:
        numba = int(numba)
        if isinstance(numba, int):
            if numba <= 0:
                print("Sorry, you must have at least 1 number")
                numba = ""
    except:
        print("You must type a number.")

symbol = ""
while symbol == "":
    symbol = input("How many SYMBOLS do you want in your password: ")
    try:
        symbol = int(symbol)
        if isinstance(symbol, int):
            if symbol <= 0:
                print("Sorry, you must have at least 1 symbol")
                symbol = ""
    except:
        print("You must use a number.")

#password generation code
password = ""

for i in range(0, alpha):
    randChar = random.randint(0, len(alphabet))
    randChar = alphabet[(randChar-1)]
    password = (password + randChar)
# making sure at least 1 upper and 1 lower case letter is used.

if len(password) == 2:
    password = (password[0].lower() + password[1].upper())
elif len(password) > 2:
    password = (password[0].lower() + password[1].upper() + password[2:-1])
else:
    print("error")


#ensuring length of requested numbers is used.

for i in range(0, numba):
    randChar = random.randint(0, len(num))
    randChar = num[(randChar-1)]
    password = (password + randChar)

#ensuring length of requested symbols is used

for i in range(0, symbol):
    randChar = random.randint(0, len(symbols))
    randChar = symbols[(randChar-1)]
    password = (password + randChar)

l = list(password)
random.shuffle(l)
password = ''.join(l)



print(f"here is your new password: {password}.")