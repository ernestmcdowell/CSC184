# Homework for CSC184-40
#
# Author: Beau McDowell
# Date: 20FEB2022
#
# Program reads in a txt file and asks the user what word they would like to count. It returns the number of times the word(case sensitive)
# Option Bonus write a program that will allow the user to replace all occurrences of a user inputted word with another word of user choice.
import re

file = open('frankenstein.txt','r', encoding='UTF-8')
open_file = file.read()
delimited_file = open_file.strip(',.;\n:').split(' ')
print(delimited_file)

def list_generator():
    lines = []
    for line in delimited_file:
        lines.append(line)
    return lines

lines = list_generator()
user_input = input("Enter the word you want to find the count of: ")

def word_counter(user_input):
    count = 0
    for element in lines:
        if(element == user_input):
            count = count +1
    print("The word: "+str(user_input)+", was found: "+str(count)+" times.")
    return count

word_to_replace = input("Please enter the word you want to replace: ")
new_word = input("Please enter the word you would like to replace it with: ")

# def word_replace(lines, old, new):
#     if lines == '':
#         return
#     if lines[0] == old:
#         return new + word_replace(lines[1:], old, new)
#     return lines[0] + word_replace(lines[1:], old, new)


word_counter(user_input)
# word_replace(lines, "the", "duck")

