import random

randomnumber = random.randint(1,10)

userguess = int( input("Guess a number between 1 and 10?") )


while(userguess != randomnumber):
    if userguess > randomnumber:
        print("The number is too big guess again")
    else:
        print("The number is too small guess again")
    
    userguess = int( input("Guess a number between 1 and 10?") )

print("Your answer is correct")

