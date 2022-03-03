# Python number guessing game( both ways)
#
# Author: Gavin Waters
#
# guess number between 1-100
import random
my_guess = -1
number_generated = random.randint(1,101)
count = 0
max_guesses = 10
while my_guess!=number_generated and count<max_guesses:
    my_guess = int(input('Please input your guess: '))
    if my_guess == number_generated and count<max_guesses - 1:
        print('Yay you are a genius!!!!')
        print('You won!!!!')
        print('The number generated was :', number_generated)
        print('You won in ',count,' tries')
        break
    elif my_guess > number_generated and count<max_guesses - 1:
        print('Your guess is too high, make it lower!!')
        print('Try again')
    elif my_guess < number_generated and count<max_guesses - 1:
        print('Your guess is too low, try someting higher!!') 
        print('try again')
    else:
        print('Incorrect and you ran out of tries, better luck next time.')
    count +=1

