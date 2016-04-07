import io,math,random,time
import numpy as np

mario = "M"
toad = "T"

wall = "#"
ground = " "
spacer = " "
marioTrail = "."
toadTrail = " "

dataDir = './maps/'

def buildCircle(r):
    y,x = np.ogrid[-r: r+1, -r: r+1]
    mask = x**2+y**2 <= r**2-1

    return mask

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

def writeBoard(board):
    serializedBoard = []
    for row in board:
        line = ""
        for cell in row:
            line += cell
        line+="\n"
        serializedBoard.append(line)
    timestr = time.strftime("%Y%m%d-%H%M%S")
    out = open(dataDir + timestr,'w')
    out.write("".join(serializedBoard))


def readBoard(fileName):
    f = open(dataDir + fileName,'r')
    board = []
    for line in list(f):
        row = []
        for cell in line:
            row.append(cell)

        board.append(row[:-1]) # remove newline
    return board
