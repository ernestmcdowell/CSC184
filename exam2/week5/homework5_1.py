# Homework for CSC184-40
#
# Author: Beau McDowell
# Date: 20FEB2022
#
# Program reads in a txt file and asks the user what word they would like to count. It returns the number of times the word(case sensitive) appears in the text.
# Optional Bonus write a program that will allow the user to replace all occurrences of a user inputted word with another word of user choice.
import string

file = open('frankenstein.txt','r', encoding='UTF-8') # opens frankenstein.txt within the working directory
open_file = file.read().translate(str.maketrans('','', string.punctuation)) # read the file and remove all punctuations
delimited_file = open_file.strip().split(' ') # strip and split file into a list
#print(delimited_file)
user_input = input("Enter a word you wish to find the count of: ") # allow user to enter a word they wish count

def word_counter(user_input):
    count = 0 # set word count to zero
    for element in delimited_file:
        if(user_input == element): # if user input word is equal to an element in the delimited file increase word count by 1
            count = count +1
    print("The word: '"+str(user_input)+"', was found: "+str(count)+" times.")

word_counter(user_input)


lines = delimited_file
old = input("Please enter the word you want to replace: ")
new = input("Please enter the word you would like to replace it with: ")

def word_replace(old, new):
    replace = ''
    for element in lines:
        if element != old:
            replace += element
        else: replace+= new
    print(replace)
    return replace

file.close() # close thee open file

word_replace(old, new)