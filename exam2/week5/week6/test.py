import random

def roll_die():
    roll = random.randint(1, 6)
    return roll

def take_turn(player):
    point=0
    keep_rolling=1
    print( " its your turn player "+str(player))
    input( "press enter to begin")
    while keep_rolling==1:
        roll = roll_die()
        print( " you got a"+str(r))
        if roll == 1:
            point=0
            keep_rolling=0
        else:
            point += roll
            print( " your total is"+str(point))
            y= input("do you want to continue? y=yes n=no")
            if y== "y":
                keep_rolling= 1
            else:
                keep_rolling= 0
    print("your turn is over")
    return point

def main():
    p1 = 0
    p2 = 0
    while p1<100 and p2<100:
        print("Player 1 points are:"+str(p1))
        print("Player 2 points are:"+str(p2))
        roll = take_turn(1)
        p1 += roll
        print("Player points are:"+str(p1))
        print("Player points are:"+str(p2))
        r = take_turn(2)
        p2 += roll
        print("The game is over")
        print("Player points are:"+str(p1))
        print("Player points are:"+str(p2))
    if p1>p2:
        print("Player one is the winner")
    elif p2>p1:
        print("player two is the winner")
    else:
        print("Tie game")



      

    




main()
take_turn(1)
take_turn(2)