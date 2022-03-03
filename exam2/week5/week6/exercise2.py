# Homework 6.1 for CSC184-40
#
# Author: Beau McDowell
# Date: 01MAR2022
#
# Game of Pig

import random
computer_inp = random.randint(1,10)


def dice():
    roll = random.randint(1,6)
    return roll

def computer_one():
    computerone_score = 0
    computer_rolling = 1
    print("CMP1 Rolling")
    while computer_rolling == 1:
        roll = dice()
        print("CMP1 rolled a: "+str(roll))
        if roll == 1:
            computerone_score = 0
            computer_rolling = 0
        else:
            computerone_score += roll
            print("CMP1 has: "+str(computerone_score)+" points this round")
            if computer_inp <= 7:
                computer_rolling = 1
            else:
                print("CMP1 Passes")
                computer_rolling = 0
    return computerone_score


def computer_two():
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
            if computer_inp <= 7:
                computer_rolling = 1
            else:
                print("CMP2 Passes")
                computer_rolling = 0
    return computertwo_score

def scores():
    comp_one = 0
    comp_two = 0
    while comp_one < 100 and comp_two < 100:
        print("CMP1 Points: "+str(comp_one))
        print("CMP2 Points: "+str(comp_two))
        roll = computer_one()
        comp_one += roll
        print("CMP1 Points: "+str(comp_one))
        print("CMP2 Points: "+str(comp_two))
        roll = computer_two()
        comp_two += roll
    if comp_one > comp_two:
        print("CMP1 is the winner")
    elif comp_two > comp_one:
        print("CMP2 is the winner")
    else:
        print("It's A Tie!")

scores()
computer_one()
computer_two()