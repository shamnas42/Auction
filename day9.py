from clear import clear_console as clear
import art

# Setting up context 
print(art.logo)
print("This is a secret aution")

# Waiting for user to start
while True:
    begin = input("Enter S to start: ")
    if begin.lower() == "s":
        clear()
        break 

# To store names and bids of people 
bids = {}

# Play until no more people to bid 
next = True
while next:
    name = input("What is your name? ")
    bid = int(input("What is your bid? "))
    more = input("Are there more bidders? Yes or No: ")

    # dict for Person : Bid
    # Focus on bid as the key for an audtion 
    bids[bid] = name
    
    # Adding more bidders 
    if more.lower() == "yes":
        next = True
        clear()
    else:
        next = False 
        clear()
        break 

# Check to see who bid the most
    
highest_bid = max(bids.keys())

# Winner 
print(f"The Winner Is {bids[highest_bid]} With ${highest_bid}.")
