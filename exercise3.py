import random

print(random.randint(1,100))

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
"""
