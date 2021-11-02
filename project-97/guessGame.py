import time
import random

print("Welcome to the Guessing Game !!")

time.sleep(1)

randomInt = int(random.random() * 9 + 1)

chances = 2

guess = int(input("Choose a number between (1 & 10) : "))

while chances <= 5:
    if not guess == randomInt:
        if not guess > 10 or guess <= 0:
            if(guess > randomInt):
                print("Incorrect !! Your Guess was too Low, guess a number higher than ",guess)

            if(guess < randomInt):
                print("Incorrect !! Your Guess was too High, guess a number lower than ",guess)
            
            chances = chances + 1
        else:
            print("Your answer was beyond the range or was an unexpexpected character. Choose a number between (1 & 10)")
        guess = int(input("Choose a number between (1 & 10) : "))
        
        
        
    if (guess == randomInt):
        print("Congratulations You Won !! Total Attempts : ", chances -1)
        print("________________________________________________________________________________________________________________________________________________________")
        break
else:
    print("You Lost !! The number was", randomInt)
    print("________________________________________________________________________________________________________________________________________________________")





