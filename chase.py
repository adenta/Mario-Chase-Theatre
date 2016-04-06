import math, boardUtils
from random import choice
from time import sleep

nextToadStep = {

'left': (-2,0),
'right': (2,0),
'up': (0,2),
'down':(0,-2),
'left and up': (-1,1),
'right and up': (1,1),
'left and down': (-1,-1),
'right and down':(1,-1)

}

BOARDSIZE = 16
board = boardUtils.buildBoard(BOARDSIZE)
toadCount = 4
steps = 0
marioMoves = [1,-1]
toadMoves = nextToadStep.keys()
def dist(p1, p2):
    return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)

def makeToad(i):
    toad = {}
    toad['id'] = i
    toad['x'] = BOARDSIZE
    toad['y'] = BOARDSIZE
    toad['distanceToMario'] = float('inf')
    toad['previousDistance'] = 0
    toad['direction'] = choice(toadMoves)
    return toad




mario = [choice(range(BOARDSIZE)),choice(range(BOARDSIZE))]
toads = [makeToad(i) for i in range(toadCount)]

def turn():
    board[mario[0]][mario[1]]=" "
    mario[0] += choice(marioMoves)
    mario[1] += choice(marioMoves)

    board[mario[0]][mario[1]]="M"
    for toad in toads:
        toad['previousDistance'] = toad['distanceToMario']
        toad['distanceToMario'] = dist(mario,[toad['x'],toad['y']])

        if toad['previousDistance'] < toad['distanceToMario']:
            toad['direction'] = choice(toadMoves)
        toadMove = nextToadStep[toad['direction']]

        board[toad['x']][toad['y']]=" "
        if not( board[toad['x'] + toadMove[0]][ toad['y'] + toadMove[1]]=="X"):
            toad['x'] += toadMove[0]
            toad['y'] += toadMove[1]

        board[toad['x']][toad['y']]="T"

        print "toad moved",toad['direction']
        print "toad",toad['id'],"is now at",[toad['x'],toad['y']],"and",toad['distanceToMario'],"away from mario,",mario,"\n"
    boardUtils.drawBoard(board)



def checkCapture():
    capture = False
    for toad in toads:
        capture = capture or toad['x'] == mario[0] and toad['y'] == mario[1]
    return capture



print "mario is at",mario
while True:
    sleep(.1)
    turn()
    steps += 1

    if checkCapture():
        break;



print "a toad found mario in",steps,"turns."
