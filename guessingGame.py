import random

number = random.randint(1,9)
chances = 0


while chances < 5 :
    guess = input("enter a number between 1-9 ")

    if int (guess) == number :
        print("You won")
        chances = 5
    else:
        if int(guess)>number :
            
             print("Guess a number greater than ", guess )
        if int(guess)<number :
             print("Guesss a number lower than ", guess)
    

    chances = chances + 1 
    




