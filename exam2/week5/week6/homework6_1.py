# Homework 6.1 for CSC184-40
#
# Author: Beau McDowell
# Date: 01MAR2022
#
# Game of Pig
# Homework for CSC184-40
#
# Author: Beau McDowell
# Date: 02MAR2022
#
# Pythong program that allows you to play The Game of Pig.

import random

def die(): # generate a random number between 1 and 6 to simulate a 6 sided die and returns the number
    roll = random.randint(1,6)
    return roll

def player_roll(current_player): # lets the player roll the die, pass or quit the game completely.
    player_score = 0
    player_turn = 1
    input("Press Enter to roll the die "+str(current_player)+" ")
    print(str(current_player)+": Rolling!")
    while player_turn == 1: # as long as player_turn is 1 run this
        roll = die() # roll the die
        print(str(current_player)+": Rolled a "+str(roll))
        if roll == 1: # if the players rolled a 1 then player_score is reset to zero for the round and end the turn for that player.
            print("Better luck next round!")
            player_score = 0
            player_turn = 0

        else: # if the player rolled anything other than a 1 then we add the rolled number to the player score
            player_score += roll
            print(str(current_player)+": "+str(player_score)+" Points this round.")
            options = input("Do you want to Roll(1), Pass(2), or Quit(3)")
            if options == "1": # allows user to roll again
                player_turn = 1
            elif options == "2": # allows user to Pass to the next player
                player_turn = 0
            elif options == "3": # allows user to quit the game entirely
                quit()
            else:
                return
    return player_score

def scores():
    points_a = 0
    points_b = 0
    while points_a < 100 and points_b < 100: # as long as points_a and points_b are less than 100 run this
        print("A Points: "+str(points_a)) # prints each players points
        print("B Points: "+str(points_b))
        roll = player_roll("Player A") # get score from the players roll and assign it to points_a
        points_a += roll 
        print("A Points: "+str(points_a))
        print("B Points: "+str(points_b))
        roll = player_roll("Player B")
        points_b += roll
    if points_a >= 100 and points_a > points_b: # if player a had more points player a wins
        print("Player A is the winner")
        quit()
    elif points_b >= 100 and points_b > points_a: # else if player b had more points player b wins
        print("Player B is the winner")
        quit()
    else: # else points are the same tie
        print("It's A Tie!")


scores()
player_roll("Player A")
player_roll("Player B")
