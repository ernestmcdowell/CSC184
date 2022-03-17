# Homework 7_1 for CSC184-40
#
# Author: Beau McDowell
# Date: 08MAR2022
#
#
# Hangman game that reads from csv file to generate a list words to select from. Allows user to guess single character or word
import random

with open('Six_letter_words.csv', 'r') as my_special_file:
    my_words = my_special_file.readlines()

    my_words = [x.strip() for x in my_words]

guessing_word = random.choice(my_words)


Hangman = ["""  
_________________
|            
|            
|           
|            
|                        
|             
|
------

_ _ _ _ _ _ 
""", """  
_________________
|            |
|            |
|           
|            
|                        
|             
|
------

_ _ _ _ _ _ 
""", """  
_________________
|            |
|            |
|           (_)
|            
|                        
|             
|
------

_ _ _ _ _ _ 
""", """  
_________________
|            |
|            |
|           (_)
|            | 
|            |            
|             
|
------

_ _ _ _ _ _ 
""", """  
_________________
|            |
|            |
|           (_)
|           /| 
|            |            
|             
|
------

_ _ _ _ _ _ 
""", """  
_________________
|            |
|            |
|           (_)
|           /|\ 
|            |            
|             
|
------

_ _ _ _ _ _ 
""", """  
_________________
|            |
|            |
|           (_)
|           /|\ 
|            |            
|           /  
|
------

_ _ _ _ _ _ 
""", """  
_________________
|            |
|            |
|           (_)
|           /|\ 
|            |            
|           / \ 
|
------

_ _ _ _ _ _ 
"""]

winner = ["""  
_________________
|
|            
|            
|          \(_)/
|           \|/
|            |            
|           / \ 
------

_ _ _ _ _ _ 
"""]

def revealed(letter_choice, unknown_word):
    word_checked = ""
    for l in unknown_word:
        if l in letter_choice:
            word_checked += l
        else:
            word_checked += "_ "
    return word_checked


def draw_hangman(choices, guessing_word):
    num_wrong_choice = 0
    for l in choices:
        if l not in guessing_word:
            num_wrong_choice += 1
    print(num_wrong_choice)
    return Hangman[num_wrong_choice]


def play():
    tries = 7 # set number of tries to 7
    guessing_word = random.choice(my_words)
    i = 0
    checked_letters = [] # empty list to store already checked letters
    bad_guesses = [] # empty list to store bad_guesses
    print(guessing_word)
    while tries > 0: #while tries is greater than 0 run this
        letter_guess = input(
            "Please enter the character you would like to guess: ") # allow user input
        if len(letter_guess) == 1: #if the length of user input is a single character 
            if letter_guess in bad_guesses or checked_letters: # user input is equal to a previous guess print message and do nothing
                print("You've already guessed that letter")
            elif letter_guess not in guessing_word: # if user guess not in the word being guessed
                i += 1 #increment i by 1
                tries -= 1 # decrease tries by 1
                bad_guesses.append(letter_guess) # append the userinput to the bad guesses list
                print("Oh no! That's is not a correct guess.")
                print("Guesses Remaining: "+str(tries))
                if tries == 0: #if tries is 0 game over print the entire word
                    print("You ran out of guesses!")
                    print("The correct word was: "+str(guessing_word))
            elif letter_guess in guessing_word: # if user guess is in the word being guessed
                print("That's Correct")
                print("Guesses Remaining: "+str(tries))
                checked_letters.append(letter_guess) # append user guess to the checked_letters list
                if all(elem in list(checked_letters) for elem in list(guessing_word)): # if all the elemens in the word beings guessed are in the checked_letters list then win
                    print(str(winner[0]).replace("_ _ _ _ _ _ ", revealed(checked_letters, guessing_word)))
                    print("You win!")
                    print("The word was: "+str(guessing_word))
                    tries = 0 
                    break
        elif len(letter_guess) == len(guessing_word): # allow user to guess the entire word guess must be 6 characters long or it's not valid input
            if letter_guess != guessing_word: #if the user guess doesn't equal the word being guessed
                i += 1 #increment i by 1
                tries -= 1 # decrease tries by 1
                bad_guesses.append(letter_guess) # append to bad guesses list
                print("Oh no! That's is not a correct guess.")
                print("Guesses: "+str(tries))
            elif letter_guess == guessing_word: # else if user guess is in the word being guessed you win
                checked_letters.append(letter_guess)
                letters = [x for x in checked_letters for x in guessing_word] # an element that is in checked letters and also in the word being guessed
                print(str(winner[0]).replace("_ _ _ _ _ _ ", revealed(letters, guessing_word)))
                break
        else:
            print("That is not a valid guess.")
        new_hang = (str(Hangman[i]).replace("_ _ _ _ _ _ ", revealed(checked_letters, guessing_word)))# replaces the occurrences of "_ _ _ _ _ _ " with value of revealed using checked letters  honestly not sure if this is how you were wanting this done. This portion was a real struggle
        print(new_hang)
    if tries == 0: # if tries are equal to zero 
        inp = input("Would you like to play again? y/n: ") # let user decide to play again or quit
        if inp == "y":
            start()
        else:
            print("Quiting")

def start():
    play()


start()
