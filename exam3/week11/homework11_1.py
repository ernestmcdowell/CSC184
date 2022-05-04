# Homework11_1 for CSC 184-40
#
# Author: Beau McDowell
# Date: 04/16/2022
#
# Finish the program by creating a computer "turn" also.
# Then create another type_player, human and human_child. This should be distinguished by age group.
# Give the child a "boost", that boost can be anything you want, just treat the humans differently by age.
#
# create the PIG game using classes and objects
import random
import time


Top_score = 20
Winner = False
all_players ={}
player_registration = True
iterations = 0


class Player:
    """ This is a class where objects get created from for players"""
    player_count = 0


    def __init__(self,name='Blank',turn_score=0,total_score=0,type_player='human',age=0):
        self.name=name
        self.turn_score=turn_score
        self.total_score= total_score
        self.type_player = type_player
        self.age = age
        Player.player_count +=1
        self.player_count = Player.player_count


    def child_player(self): # definiton for a child player assigning a human_child type_player and giving a +5 bonus to the total score at the start of the game
        self.type_player = "human_child"
        self.total_score = 5
        return self.type_player, self.age 


print()
print('Welcome to the game of PIG, Please eneter your players')
print()
print('All children under the age of 16 get a 5 point starting bonus. All other players start at 0.')



while player_registration:
    name_input = input('Please enter the players name, or "C" for a computer player, or "Q" to quit entering players :')
    player_age = int(input("Please enter the players age: ")) # ask user to input the players age
    enter_more = input("Do you want to add more players? Y/n : ") # ask if entering more players into the game
    if name_input == "C" or name_input == "c": # if name == c or C the player is a computer
        player1 = Player(name="Computer_"+str(Player.player_count+1),type_player="Computer")
        all_players.update({"Computer_"+str(Player.player_count):player1})
    else: # else if the name is anything else the player will be a human or human_child type_player
        if player_age <= 15: # if the age of the player is less than or equal to 15 they are of type_player human_child
            child = Player(name = name_input)
            child.child_player() # calls the child_player function to set the bonus and type_player
            all_players.update({"child_"+str(Player.player_count):child}) 
        elif player_age > 15: # if age is greater than 15 then the player is of type_player human and no bonus i given
            player1 = Player(name = name_input)
            all_players.update({"player_"+str(Player.player_count):player1}) 
    if enter_more =="N" or enter_more =='n': # stops the entering or more players
        print('end of players')
        break
    print('Thanks, that player has been registered.')

for p in all_players.keys():
    print(p, all_players[p].name, all_players[p].type_player)

def human_player(player):
    print()
    print('It is the turn of :',player.name)
    print('Their present score is ',player.total_score)
    print()
    player.turn_score=0
    roll = 'yes'
    while roll != "Q" or roll != 'q':
        roll = input('please press "Q" to stop and enter to roll :')
        if roll =="Q" or roll =='q':
            print('you have ended your turn')
            break
        else:
            dice_roll = random.randint(1,6)
            if dice_roll ==1:
                print("Awwwww, you rolled a 1 ")
                print()
                time.sleep(1)
                player.turn_score = 0
                break
            else:
                player.turn_score += dice_roll
                print('You rolled a ',dice_roll)
                print()
                print('Your current turn score is ',player.turn_score, ' with your total being ',player.total_score + player.turn_score)
                print()
    player.total_score += player.turn_score


def computer_player(computer):
    print()
    print('It is the turn of :',computer.name)
    print('Their present score is: ',computer.total_score)
    print()
    computer_inp = random.randint(1,3) # assigns a random integer between 1 and 3 for decision making
    computer.turn_score=0
    isRolling = True
    while isRolling: # run this while isRolling is True
        dice_roll = random.randint(1,6)
        time.sleep(2) # creates a 2 second delay between dice rolls
        if dice_roll ==1:
            print(str(computer.name)+" rolled a 1 ")
            print()
            computer.turn_score = 0
            break
        else:
            computer.turn_score += dice_roll
            print(str(computer.name)+' rolled a ',dice_roll)
            print()
            print(str(computer.name)+' turn score is: ',computer.turn_score, ' with a total score of:  ',computer.total_score + computer.turn_score)
            print()
        if computer_inp == 1: # if the computer_inp is equal to a 1 the computer will roll again
            isRolling = True
        else: # if the computer_inp is equal to anyting other than a one the computer will pass their turn.
            print(str(computer.name)+" passes their turn")
            isRolling = 0
    computer.total_score += computer.turn_score


while Winner ==False:
    for p in all_players.keys():  
        time.sleep(0.5)
        print('      ******* New Player!!!********  ')
        if all_players[p].type_player=="human" or all_players[p].type_player=="human_child":
            human_player(all_players[p])
            if all_players[p].total_score >= Top_score:
                print()
                print('We have a winner!!!')
                print(all_players[p].name,' won the game!!!! Hurray')
                Winner=True
                break
        else:
            computer_player(all_players[p])
            if all_players[p].total_score >= Top_score:
                print()
                print('We have a winner!!!')
                print(all_players[p].name,' won the game!!!! Hurray')
                Winner=True
                break



