import random

userinput = int( input("Pick a number between 1 and 6") )

diceroll = random.randint(1,6)

while userinput != diceroll:
    print(f"The diceroll was {diceroll}. Try again.")

    userinput = int( input("Pick a number between 1 and 6") )

    diceroll = random.randint(1,6)


print("You have successfully rolled " + str( diceroll))