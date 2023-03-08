"""
Exercise 3: "Guess the number" game
1) The script will generate a "secret" integral number in
the range [1,100]:
    function to use is "randint()"
    the module that contains the function is "random"
    
2) Then the script will prompt you for an int
    (use the function input() combined with int())
    
3) According to the value entered (using a if/elif/else statement), 
the script will print (print() function) the message:
        "Too large"
        "Too small"
        "Bingo!"
        
You will have up to 6 attempts to find the secret number 
(use a while loop to repeat step 2 and 3 up to 6 times)
"""

import random

secret=random.randint(1,100)

print(secret)

currentNumberOfAttempts=0

while currentNumberOfAttempts < 6:
    #currentValue=input("Enter an int in the range [1,100] (1/6): ")
    currentValue=input(f"Enter an int in the range [1,100] ({currentNumberOfAttempts+1}/6): ")
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
    print(f"The secret number was: {secret}")