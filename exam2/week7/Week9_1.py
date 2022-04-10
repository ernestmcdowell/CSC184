# Exam2 for CSC-184-40
#
# Date: 3/29/2022
# Author: Ernest B McDowell
#
# WORDLE

from termcolor import colored #pip install termcolor 
import json
from collections import Counter
import random
import csv

########################finding words from our dictionary ######################

my_file = open('dictionary.json','r')
my_dict = json.load(my_file)
my_words = list(my_dict.keys())
my_words = [x.lower() for x in my_words if len(x)==5 and x.isalpha()]
my_definitions = list(my_dict.values())

my_def_words =[]
for my_defs in my_definitions: 
    my_defs= my_defs.strip()
    my_defs= my_defs.split()
    my_defs = [x.lower() for x in my_defs if len(x)==5 and x.isalpha()]
    my_def_words.append(my_defs)

my_def_words = [word for mini_list in my_def_words for word in mini_list]
my_occurances = dict(Counter(my_def_words))
my_nums = list(my_occurances.values())
my_nums.sort()
my_wordle_words = [x for x in my_occurances if my_occurances[x]>=my_nums[85*len(my_nums)//100]]
my_allowable_words = list(set(my_def_words).union(set(my_words)))
my_new_file = open('My_all_5_words.csv','w', newline='') # windows machines screw things up
my_csv_writer = csv.writer(my_new_file)

for w in my_allowable_words:
    my_csv_writer.writerow([w])

################# Hints on exam #####################
tries = 6
wordle_word = random.choice(my_wordle_words) # 'bench'
wordle_color = []
word_colored = ['grey','grey','grey','grey','grey']
my_letter_chosen = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
my_letter_chosen_color = []
for l in my_letter_chosen:
    my_letter_chosen_color.append('grey')
for l in wordle_word:
  wordle_color.append('green')

# I thought i was on the right track to change the letter colors but i couldn't get this part to work
def letter_selection(my_letter_chosen,my_guessing_word,my_letter_chosen_color,wordle_word):
    wordle_word=wordle_word.upper()
    my_guessing_word = my_guessing_word.upper()
    for count in range(0,len(my_letter_chosen)):
        if my_guessing_word not in wordle_word:
            my_letter_chosen_color = ['grey' for i in my_guessing_word]

        if my_guessing_word in wordle_word: # change color to yellow if my_guessing_word in wordle_word but not same index
            my_letter_chosen_color = ['yellow' for i in my_guessing_word]

        if my_guessing_word == wordle_word: # change color to green if my_guessing_word is equal wordle_word
            my_letter_chosen_color = ['green' for i in my_guessing_word]

        print(colored(my_letter_chosen[count].upper(),my_letter_chosen_color[count]),end=' ')
    return colored(my_letter_chosen[count].upper(),my_letter_chosen_color[count])

def letter_color(tries,wordle_word,my_guessing_word,my_letter_chosen_color,word_colored):
    wordle_word=wordle_word.upper()
    my_guessing_word = my_guessing_word.upper()
    while tries > 0: # run this if tries bigger than 0
        print("You have "+str(tries)+" remaining.")
        for count in range(0,len(word_colored)):
            letter_indx = my_letter_chosen.index(my_guessing_word[count])
            if my_guessing_word not in wordle_word:
                word_colored = ['grey' for i in my_guessing_word] # change color to grey if my_guessing_word not in wordle_word
                if my_guessing_word[count] in wordle_word: # change color to yellow if my_guessing_word in wordle_word but not same index
                    word_colored = ['yellow' for i in my_guessing_word]
            if my_guessing_word[count] == wordle_word[count]: # change color to green if my_guessing_word is equal wordle_word
                word_colored = ['green' for i in my_guessing_word]
            print(colored(my_guessing_word[count],word_colored[count]),end=' ')
            print(my_guessing_word[count],wordle_word[count],word_colored[count], my_letter_chosen.index(my_guessing_word[count]))
        letter_selection(my_letter_chosen,my_guessing_word[count],my_letter_chosen_color,wordle_word[count])
        return word_colored, my_letter_chosen_color
    return my_guessing_word

def main(tries,my_letter_chosen_color,word_colored):    
    wordle_word = random.choice(my_wordle_words)
    print(wordle_word)
    Game_finished=False
    print("You have "+str(tries)+" tries remaining.")
    while Game_finished == False:
        my_guessing_word = input('please input your word, input "q" to quit : ')
        tries -=1
        if my_guessing_word=="q":
            print('Thanks for playing!')
            Game_finished = True
            break
        elif my_guessing_word == wordle_word:
            print("That's right! The word was "+colored(wordle_word.upper(), wordle_color[0])+".")
            print("You Win!")
            tries = 6
            inp = input("Would you like to play again? y/n: ") # let user decide to play again or quit
            if inp == "y":
                print("reseting")
                main(tries,my_letter_chosen_color,word_colored)
            else:
                print("Good Bye!1")
                quit()
        elif tries == 0: # if tries are equal to zero allow user to quit or play again
            print("Oh No! You ran out of tries!")
            print("The word was "+colored(wordle_word.upper(), wordle_color[0]),end=' ')
            inp = input("Would you like to play again? y/n: ") # let user decide to play again or quit
            if inp == "y":
                main(tries,my_letter_chosen_color,word_colored)
            else:
                print("Good Bye!")
                exit()
        else:
            if my_guessing_word in my_allowable_words:
                word_colored, my_letter_chosen_color =  letter_color(tries,wordle_word,my_guessing_word,my_letter_chosen_color,word_colored)
            else:
                print("you entered a incorrect word")
    if Game_finished == True:
            exit()


main(tries,my_letter_chosen_color,word_colored)