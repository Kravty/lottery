# Program simulates lottery, where six numbers (out of 49) are selected.
# Each correct guess of the user is counted and total score is printed.

import random as r

lottery_numbers = []
choices = []

while len(lottery_numbers) != 6:
    number= r.randrange(1, 50)
    if number not in lottery_numbers:
        lottery_numbers.append(number)

order = 1  # Variable used for printing order of guesses
while len(choices) != 6:
    choice = input('Pick your '+str(order)+' lottery number (from 1 to 49). \n')
    # Error handling with non-integer input
    try:
        choice=int(choice)  
        # Error handling with incorrect guess range         
        if choice not in choices:    
            if 0 < choice < 50:
                choices.append(choice)
                order += 1
            else:
                print('The number should be between 1 and 49.')
        else:
            print('You have already picked that number.')
    except:
        print('Incorrect number. Please type a number.')

score = 0  # Variable used for counting correct numbers
for value in range(0, 6):
    if choices[value] in lottery_numbers:
        score += 1
        print('Congratulations! Chosen number', choices[value], 'is one of lottery numbers!')

if score == 0:
    print('Unfortunatelly, none of picked numbers was a lottery number.')
else:
    print('Congratulations! You have guessed', score, 'of lottery numbers!')

lottery_numbers.sort()
print('Lottery numbers are:', lottery_numbers)