# Lesson 8 follow along
#
# Date 3/10/2022
#

import json
import random

my_file = open('../week7/dictionary.json','r')
my_dict = json.load(my_file)
my_words = list(my_dict.keys())
my_words = [x.lower() for x in my_words if len(x)==6 and x.isalpha()]

print(my_words)

for word in my_words[30:60]:
    print(word, my_dict[word])

my_definitions = list(my_dict.values())


my_def_words = []
for defs in my_definitions:
    defs = defs.strip()
    defs = defs.split()
    defs =[x.lower() for x in defs if len(x)==6 and x.isalpha()]
    my_def_words.append(defs)

my_def_words = [word for mini_list in my_def_words for word in mini_list] # takes words in sub lists and puts them in one large list

for x in range(0,10): # print random words from my_def_words
    print(random.choice(my_def_words))

my_occurances = {}

for word in my_words:
    my_occurances.update({word:my_words.count(word)})
    # print(my_occurances)

from collections import Counter

my_occurances = dict(Counter(my_def_words))

my_nums = list(my_occurances.values())

my_nums.sort()

print(len(my_nums))
print(my_nums[-390])

my_wordle_words = [x for x in my_occurances if my_occurances[x] >= 27]

print(len(my_wordle_words))

import csv


my_new_file = open('worlde_words.csv','w')
my_csv_writer = csv.writer(my_new_file)

for w in my_wordle_words:
    my_csv_writer.writerow([w])
my_wordles = []