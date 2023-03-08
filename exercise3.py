"""
Write a Python scripts that implements the “Guess the Number” game.
The script will generate of a random integral number (use the module random) 
from 1 to 100, and ask you to guess it.
The script will tell you if each guess is too high or too low.
You win if you can guess the number within six tries.

To generate the secret random int:
    import random
    random.randint(1,100)
To prompt the user for an int:
    input() + int()
To prompt the user for multiple int:
    use a while loop that will embed the input() function
    in the loop an if statement will be used to compare
    the value entered with the secret number
    You leave this loop either because the secret number is found or 
    because the max number of attempts to guess it is reached
"""
import random
secret=random.randint(1,100)

print(secret)

currentNumberOfAttempts=0

while currentNumberOfAttempts < 6:
    currentValue=input("Enter an int in the range [1,100]: ")
    currentValue=int(currentValue)
    if currentValue == secret:
        print ("Bingo ! You've found the secret number")
        break
    elif currentValue > secret:
        print("Too large !")
    elif currentValue < secret:
        print("Too small !")   
    currentNumberOfAttempts = currentNumberOfAttempts + 1
    
if secret != currentValue:
    print("The secret number was:", secret)