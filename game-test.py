#!
# -*- coding:utf-8 -*-

import time
from os import system


Coordinate:list[int]=[1,-1]


def cb0(m,n):
    match n: 
        case 0: # top
            match m:
                case 0:
                    return "┏━━"
                case 14:
                    return "┓"
                case _:
                    return "┳━━"
        case 14: # buttom
            match m:
                case 0:
                    return "┗━━"
                case 14:
                    return "┛"
                case _:
                    return "┻━━"
        case _: # center
            match m:
                case 0:
                    return "┣━━"
                case 14:
                    return "┫"
                case _:
                    return "╋━━"



class Player:
    def __init__(self,name,game,n):
        self.playername=name
        self.playgame=game
        self.n=n
    def run(self,x,y):
        
        #print(self.playgame.checkerboard)
        self.playgame.checkerboard[x][y]=self.n
        print(f'[{time.strftime("%H:%M:%S",time.localtime())}]Player "{self.playername}" go to ({x},{y}).')



class Checkerboard:

    def __init__(self,x):
        self.checkerboard=[]
        for i in range(0,15):
            self.checkerboard.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,])
        print(f'[{time.strftime("%H:%M:%S",time.localtime())}]Create a chessboard.')
        
    def p(self,Coordinate):
        """
        ●○
        ┏━┳━┓
        ┣━╋━┫
        ┗━┻━┛
        ┏━●━┓
        ┣━╋━○
        ┗━┻━┛
        """
        for n in range(0,15):
            # print(n)
            for m in range(0,15):
                if self.checkerboard[n][m]==0:
                    print(cb0(m,n),end="")
                elif self.checkerboard[n][m]==Coordinate[0]:
                    print("●━━",end="")
                elif self.checkerboard[n][m]==Coordinate[1]:
                    print("○━━",end="")
            print("\n")
        


def resolve_coordinates(s):
    x=int(s.split(',')[0][1:])
    y=int(s.split(',')[1][:-1])
    return x,y

def check_the_coordinates(game,x,y,player):
    if game.checkerboard[x][y]!=0:
        print(f'[{time.strftime("%H:%M:%S",time.localtime())}][ERR] "{player.playername}" You can\'t come here! ({x},{y}).')
        return True


a=Checkerboard(15)
per1=Player(name=input('Player 1 name:'),game=a,n=Coordinate[0])
per2=Player(name=input('Player 2 name:'),game=a,n=Coordinate[1])
print(f'[{time.strftime("%H:%M:%S",time.localtime())}]Games start.')


def row(a): # --
    for line in range(0,len(a)):
        for i in range(0,len(a)-4):
            l=[a[line][i],a[line][i+1],a[line][i+2],a[line][i+3],a[line][i+4]]
            #print("row:",l)
            v=victory_rules(l)
            #print(v)
            if (v == -1) or (v == 1):
                return v


def column(a): # |
    for line in range(0,len(a)-4):
        for i in range(0,len(a)):
            l=[a[line][i],a[line+1][i],a[line+2][i],a[line+3][i],a[line+4][i]]
            #print("column:",l)
            v=victory_rules(l)
            #print(v)
            if (v == -1) or (v == 1):
                return v


def rc(a): # /
    for line in range(0,len(a)-4):
        for i in range(5,len(a)):
            l=[a[line][i],a[line+1][i-1],a[line+2][i-2],a[line+3][i-3],a[line+4][i-4]]
            #print("row-column:",l)
            v=victory_rules(l)
            #print(v)
            if (v == -1) or (v == 1):
                return v


def cr(a): # \
    for line in range(0,len(a)-4):
        for i in range(0,len(a)-4):
            l=[a[line][i],a[line+1][i+1],a[line+2][i+2],a[line+3][i+3],a[line+4][i+4]]
            #print("column-row:",l)
            v=victory_rules(l)
            #print(v)
            if (v == -1) or (v == 1):
                return v


# row-, column|, rc\, cr /
def victory_rules(l:list):
    ks:list=[[1,1,1,1,1],[-1,-1,-1,-1,-1],[0,0,0,0,0]]
    d={0:1,1:-1,2:0}
    for k in range(0,3):
        #print("k:",ks[k])
        if ks[k] == l:
            return d[k]


def game_over(player):
    print(f'[{time.strftime("%H:%M:%S",time.localtime())}][END]"{player.playername}" You are victorious!!')
    a.p(Coordinate)


if __name__ == '__main__':
    victory=False
    while victory==0:
        for per in [per1,per2]:
            while True:
                # system('cls') # clear
                a.p(Coordinate)
                xy=input(f'[{time.strftime("%H:%M:%S",time.localtime())}]Player "{per.playername}" go to(x,y):')
                x,y=resolve_coordinates(xy)
                if check_the_coordinates(a,x,y,per)==True:
                    continue
                per.run(x,y)
                break
            #print(a.checkerboard)
            match (
            cr(a.checkerboard) or 
            rc(a.checkerboard) or 
            column(a.checkerboard) or 
            row(a.checkerboard)):
                    case per1.n:
                        victory=game_over(per1)
                        break
                    case per2.n:
                        victory=game_over(per2)
                        break

