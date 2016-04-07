import io,math,random
import numpy as np

wall = "#"
ground = " "
spacer = " "
marioTrail = "m"
toadTrail = "t"

def buildCircle(r):
    y,x = np.ogrid[-r: r+1, -r: r+1]
    mask = x**2+y**2 <= r**2-1

    return mask
def drawCircle(circle):
    for row in circle:
        st = ""
        for col in row:
            if col and random.randint(0,100)>5 :
                st+= " "
            else:
                st+= "#"
        print st

def buildBoard(n):
    circle = buildCircle(n);
    board = []

    for row in circle:
        board.append([ground if cell else wall for cell in row])

    return board

def drawBoard(board):
    for row in board:
        st = ""
        for cell in row:
            st += spacer + cell
        print st
