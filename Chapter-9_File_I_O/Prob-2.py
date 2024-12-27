'''The game() function in a prog. lets a user play a game & returns the 
score as an integer. You need to read file 'Hi-score.txt' which is eithere 
blank are contains previous Hi-score . You need to WAP to update Hi-score 
whenever game() funct" breeaks the Hi-score.'''

import random

def game():
    print("You are Playing Game!")
    score = random.randint(1,62)
    # Fetch Your Score
    with open('Hi-sccore.txt') as f:
        hiscore = f.read()
        if hiscore != "":
            hiscore = int(hiscore)
        else:
            hiscore = 0
    print(f"Your Score: {score}")
    if(score > hiscore):
        # Write this hiscore to the file, if hiscore is greater than score
        with open('Hi-sccore.txt','w') as f:
            f.write(str(score))
    return score

# Call the game function
game()

# Explanation:
'''The selected code defines a function called `game()`. This function 
simulates a game where a player's score is generated randomly between 
1 and 62. The function reads the current high score from a file named 
'Hi-sccore.txt'. If the file is not empty, the high score is converted
 to an integer; otherwise, the high score is set to 0.

After generating the player's score, the function compares it with the 
current high score. If the player's score is greater than the current 
high score, the player's score is written to the 'Hi-sccore.txt' file,
effectively updating the high score.

Finally, the function returns the player's score.

This code snippet demonstrates how to read from a file, compare values, 
and write to a file in Python. It also showcases the use of conditional 
statements and file handling.'''