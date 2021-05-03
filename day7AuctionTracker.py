# get the number of bidders in the auction
bidders = ""
while bidders == "":
    bidders = input("How many bidders: ")
    try:
        bidders = int(bidders)
        if isinstance(bidders, int):
            if bidders <= 0:
                print("You must have at least 1 bidder.")
                bidders = ""
            else:
                print(f"There are {bidders} bidders.")

    except:
        print("You must type a whole number (1, 2, 3... etc.).")
        bidders = ""

# Dictionary to story the values of bidder inputs
numbidders = {}
for i in range(1, bidders + 1):
    i = str(i)
    numbidders['bidder ' + i] = "blank value"

for i in range(1, len(numbidders) + 1):
    i = str(i)
    while not isinstance(numbidders['bidder ' + i], int):
        numbidders['bidder ' + i] = input(f"what is {('bidder ' + i)}'s bid: ")
        try:
            numbidders['bidder ' + i] = int(numbidders['bidder ' + i])
        except:
            print(f"{('bidder ' + str(int(i) + 1))} should be a number.")

#determine the highest bidder / amount paid
highestBid = 0
for bidder in numbidders:
    numbidders[bidder] = int(numbidders[bidder])
    if numbidders[bidder] > highestBid:
        highestBid = numbidders[bidder]
        winner = bidder

print(f"{winner} is our winner, and offered {highestBid}!")