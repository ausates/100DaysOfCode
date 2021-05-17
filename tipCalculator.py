#Tip Calculator
import time
print("Let's figure out the bill here, shall we?")
time.sleep(.5)

# get total bill
totalBill = 0
while totalBill == 0:
    totalBill = input("What is your total bill: $")
    try:
        totalBill = float(totalBill)
    except:
        print("Your bill must be a number.")
        totalBill = 0

# get total number of people to split bill among

numPeople = 0
while numPeople == 0:
    numPeople = input("How many people will be splitting the bill: ")
    try:
        numPeople = int(numPeople)
        if numPeople == 0:
            print("The number of people must be greater than 0")
            numPeople = 0
            pass
        elif numPeople < 0:
            print("The number of people must be greater than 0")
            numPeople = 0
            pass
    except:
        numPeople = 0
        print("The number of people must be a whole number.")

# get tip amount

tipAmount = True

while tipAmount == True:

    tipAmount = input("What tip percent would you like to leave: ")
    try:
        tipAmount = int(tipAmount)
        if tipAmount < 0:
            print("The tip amount must be 0 or higher.")
            tipAmount = True
            pass
    except:
        tipAmount = True

# what each person pays

tipA = ((tipAmount/100) * totalBill)
tipB = round(tipA, 2)
payPerPerson = ((totalBill + tipA) / numPeople)
payPerPerson = round(payPerPerson, 2)
print(f"The total tip = {tipB}.")
print(f"The total bill after tip = {(totalBill + tipB)}")
print(f"There are {numPeople} people paying.")
print(f"Each person pays {payPerPerson}.")
