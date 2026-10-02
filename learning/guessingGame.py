#This is a guess the number game.
import random

# Get the player's name.
print('Hello. What is your name?')
name = input()

#Main game loop
while True:
    secretNumber = random.randint(1, 20) # Generate a random number between 1 and 20
    print('Well, ' + name + ', I am thinking of a number between 1 and 20 can you guess it in six tries?')
    #Allow the player to guess 6 times.
    for guesses in range(1, 7):
        print('Take a guess.')
        guess = int(input()) # Get the player's guess
        
        # Check if the guess is too low, too high, or correct
        if guess < secretNumber:
            print('Your guess is too low.')
        elif guess > secretNumber:
            print('Your guess is too high.')
        else:
            break
    if guess == secretNumber: # If the guess is correct
        print('Good job, ' + name + '! you guessed my number in ' + str(guesses) + ' tries')
    else: # If the guess is incorrect after 6 tries
        print('Hard luck, the number I was thinking of was ' + str(secretNumber))
    print('Would you like to play again?(y,n)')
    y = input() # Get the player's response
    
    # If the player does not want to play again, exit the loop
    if y == 'n' or y == 'N':
        break
