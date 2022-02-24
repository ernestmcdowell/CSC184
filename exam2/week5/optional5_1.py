# Homework for CSC184-40
#
# Author: Beau McDowell
# Date: 20FEB2022
#
#Optional Bonus(no points) write a program that will allow the user to replace all occurrences of a user inputted word with another word of user choice.
import string

file = open('frankenstein.txt','r', encoding='UTF-8') # opens frankenstein.txt within the working directory
open_file = file.read().translate(str.maketrans('','', string.punctuation)) # read the file and remove all punctuations
delimited_file = open_file.strip().split(' ') # strip and split file into a list


#OPTIONAL
# Optional section for replacing a word. I was unable to get the text to format properly
def word_replace():
    old = input("Please enter the word you want to replace: ")
    new = input("Please enter the word you would like to replace it with: ")
    new_file = open('new.txt','w')
    replace = '' # empty string
    for element in delimited_file:
        if element != old: # if the element in the delimited file does not equal the user input for old.
            replace += element #  Then empty string replace takes on the value of the current element and nothing gets changed
        else: replace += new # else if the element is equal to the user input of old, replace takes on the value of user input for new
    new_file.write(replace)
    new_file.close()
# was unable to get the written file to contain spaces between words
#

word_replace() # call word_replace function