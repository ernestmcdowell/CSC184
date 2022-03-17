# Dictionaries, json, csv and Hangman
#
# Date: 3/2/2022
#
# Gavin Waters
import random
import csv 

with open('Six_letter_words.csv','r') as my_special_file:
    my_words = my_special_file.readlines()
    my_words = [x.strip() for x in my_words]
guessing_word =random.choice(my_words)


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
""","""  
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
""","""  
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
""","""  
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
""","""  
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
""","""  
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


def revealed(letter_choice,unknown_word):
    word_checked = ""
    for l in unknown_word:
        if l in letter_choice:
            word_checked += l
        else:
            word_checked +="_"
        
    return word_checked
def draw_hangman(choices, guessing_word):
    num_wrong_choice=0
    for l in choices:
        if l not in guessing_word:
            num_wrong_choice += 1
    print(num_wrong_choice)
    return Hangman[num_wrong_choice]
    
print(guessing_word)
print(revealed(["a",'e','c','i'], guessing_word))
print(draw_hangman(["a",'e','c','i'], guessing_word))