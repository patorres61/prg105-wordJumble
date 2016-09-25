# Phyllis Torres
# Word Jumble
# This program provides a list of vegetables that will randomly be selected for scrambling and displayed for the user.
# The user will then have an opportunity to guess the answer until they guess the correct answer.

# import the random library
import random

# define colors and bold text parameters
class color:
    def __init__(self):
        pass
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

# Create a list of words and initialize variables
veggies = ['ARUGULA', 'ASPARAGUS', 'BEETS', 'BROCCOLI', 'CABBAGE', 'CARROTS', 'CAULIFLOWER', 'EGGPLANT', 'ENDIVE', 'LEEKS', 'LETTUCE', 'OKRA', 'ONIONS', 'PEAS', 'RADISHES', 'SPINACH', 'SQUASH', 'WATERCRESS', 'YAM', 'ZUCCHINI']
correct = ''

# Random Choice
# Reference: https://docs.python.org/2/library/random.html
selection = random.choice(veggies)
answer = selection

# program title, describe the program and print instructions for the user
print color.BOLD + '                                 WORD JUMBLE GAME\n\n' + color.END
print ('\n\nThe topic of this program is Vegetables! This program will randomly select a vegetable and jumble it. ' +
       'Your job, should you choose to accept it, is to unscramble the word and enter the correct answer.\n')
print ('You do not need to worry about upper or lower case when typing in your answer, just the correct spelling.\n')

# program chooses a word to jumble
jumble = list(selection)

# the following code will scramble the letters for the selected word from the jumble list
for current_index in range(len(jumble)):
    random_index = random.randrange(0, len(jumble))
    temp = jumble[current_index]
    jumble[current_index] = jumble[random_index]
    jumble[random_index] = temp

# print out the scrambled letters
for letter in jumble:
    print color.BOLD + letter + color.END,  # the comma omits the new line

# accept the user's guess as input
guess = raw_input('\n\nWhat kind of vegetable is jumbled? ')
guess = guess.upper()

# the variable, correct, will keep track of whether or not the user input is correct
# if the guess is incorrect, the variable will be set to "no"
# if the guess is correct, the variable will be set to "yes"
# while the user's guess is not correct, the loop will continue to prompt the user for another guess
while correct != 'yes':
    if guess == answer:
        print ('\nYou are correct! The answer is: ' + answer)
        correct = 'yes'
    else:
        correct = 'no'
        print ('\nThat is not correct! Double check the scrambled letters and try again.')
        guess = raw_input('\nWhat kind of vegetable is jumbled? ')
        guess = guess.upper()

print ("\n\nThank you for playing! And, remember...Eat your veggies!!!")
