# Homework 6.1 for CSC184-40
#
# Author: Beau McDowell
# Date: 01MAR2022
#
# Game of Pig Between two computers (OPTIONAL)
# Doesn't work everytime sometimes it seems like it will run forever without getting a winner 


import random
computer_inp = random.randint(1,10) # generate random number between 1 and to to use for input


def dice(): # generate a random number between 1 and 6 to simulate a 6 sided die and returns the number
    roll = random.randint(1,6)
    return roll

def computer_one(): # let computer either roll the die or pass their turn
    computerone_score = 0
    computer_rolling = 1
    print("CMP1 Rolling")
    while computer_rolling == 1:
        roll = dice()
        print("CMP1 rolled a: "+str(roll))
        if roll == 1: # if computer rolls a one score is wipe to 0 and computer_rolling is zero other computers turn
            computerone_score = 0
            computer_rolling = 0
        else:
            computerone_score += roll # if the result of roll is anything other than a 1 add the results to computer_score
            print("CMP1 has: "+str(computerone_score)+" points this round")
            if computer_inp <= 6: # if computer input is less than or equal to 7 computer will roll again
                computer_rolling = 1
            else: # else if computer input is greater than 7 computer passes their turn
                print("CMP1 Passes")
                computer_rolling = 0
    return computerone_score


def computer_two(): # same as computer_one function other than variable names
    computertwo_score = 0
    computer_rolling = 1
    print("CMP2 Rolling")
    while computer_rolling == 1:
        roll = dice()
        print("CMP2 rolled a: "+str(roll))
        if roll == 1:
            computertwo_score = 0
            computer_rolling = 0
        else:
            computertwo_score += roll
            print("CMP2 has: "+str(computertwo_score)+" points this round")
            if computer_inp <= 6:
                computer_rolling = 1
            else:
                print("CMP2 Passes")
                computer_rolling = 0
    return computertwo_score

def scores():
    comp_one = 0
    comp_two = 0
    while comp_one < 100 and comp_two < 100: # run this as long as points are less than 100
        print("CMP1 Points: "+str(comp_one))
        print("CMP2 Points: "+str(comp_two))
        roll = computer_one() # get score from computer_one 
        comp_one += roll # add result of roll to comp_one to get total score for comp_one
        print("CMP1 Points: "+str(comp_one))
        print("CMP2 Points: "+str(comp_two))
        roll = computer_two()
        comp_two += roll
    if comp_one >= 100 and comp_one > comp_two: # if comp one scored higher comp one wins
        print("CMP1 is the winner")
        quit()
    elif comp_two >= 100 and comp_two > comp_one: # if comp two scored higher comp two wins
        print("CMP2 is the winner")
        quit()
    else:
        print("It's A Tie!")


scores()
computer_one()
computer_two()