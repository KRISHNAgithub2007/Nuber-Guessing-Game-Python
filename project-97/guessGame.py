import time
import random

print("Welcome to the Guessing Game !!")

time.sleep(1)

max = 10

chances = 2

print("Choose Difficulty Level ----")
print("1 = easy")
print("2 = normal")
print("3 = hard")

difficulty = int(input("Difficulty : "))

if(difficulty == 1):
    max = 10
elif(difficulty == 2):
    max = 20
elif(difficulty == 3):
    max = 30
while (difficulty <= 0 or difficulty >= 4):
    print("Choose Difficulty Level between (1 & 3)")
    difficulty = int(input("Difficulty : "))


randomInt = int(random.random() * (max - 1) + 1)

guess = int(input("Choose a number between (1 & " + str(max) + ") : "))



while chances <= 5:
    if not guess == randomInt:
        if not guess > max or guess <= 0:
            if(guess > randomInt):
                print("Incorrect !! Your Guess was too High, guess a number lower than ",guess)

            if(guess < randomInt):
                print("Incorrect !! Your Guess was too Low, guess a number higher than ",guess)
            
            chances = chances + 1
        else:
            print("Your answer was beyond the range or was an unexpexpected character. Choose a number between (1 & max)")
        guess = int(input("Choose a number between (1 & " + str(max) + ") : "))
        
        
        
    if (guess == randomInt):
        print("Congratulations You Won !! Total Attempts : ", chances - 1)
        print("________________________________________________________________________________________________________________________________________________________")
        break
else:
    print("You Lost !! The number was", randomInt)
    print("________________________________________________________________________________________________________________________________________________________")





