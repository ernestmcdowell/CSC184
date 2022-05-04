# Pig game again with objects
#
# Author: Gavin Waters
#
# create the PIG game using classes and objects
import random
import time

Top_score = 20

class Player:
    """ This is a class where objects get created from for players"""
    player_count = 0

    def __init__(self,name='Blank',turn_score=0,total_score=0,age=0,type_player='human'):
        self.name=name
        self.turn_score=turn_score
        self.total_score= total_score
        self.type_player = type_player
        self.age = age
        Player.player_count +=1
        self.player_count = Player.player_count

    def child_player(self):
        if self.age <= 15:
            self.total_score = 5
        
all_players ={}
print()
print('Welcome to the game of PIG, Please eneter your players')
print()

player_registration = True

while player_registration:
    print()
    name_input = input('Please enter the players name, or "C" for a computer player, or "Q" to quit entering players :')
    if name_input == "C" or name_input == "c":
        player1 = Player(name="Computer_"+str(Player.player_count+1),type_player="Computer")
        all_players.update({"player_"+str(Player.player_count):player1})
    elif name_input =="Q" or name_input=='q':
        print('end of players')
        break
    else:
        player1 = Player(name = name_input)
        player_age = input("Please enter the players age")
        player_age = Player(age = player_age)
        all_players.update({"player_"+str(Player.player_count):player1})
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

def computer_player(player):
    print()
    
Winner = False
while Winner ==False:
    for p in all_players.keys():
        time.sleep(0.5)
        print('      ******* New Player!!!********  ')
        if all_players[p].type_player=="human":
            human_player(all_players[p])
            if all_players[p].total_score > Top_score:
                print()
                print('We have a winner!!!')
                print(all_players[p].name,' won the game!!!! Hurray')
                Winner=True
                break
        else:
            print("computer turn")
            time.sleep(1)