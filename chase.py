import math, boardUtils, io
from random import choice
from time import sleep

inputFlag = False

if not inputFlag:

    BOARDSIZE = 14
    board = boardUtils.buildBoard(BOARDSIZE)

else:
    while True:
        userBoard = raw_input("What board do you want to use?")
        try:
            board = boardUtils.readBoard(userBoard)
            break
        except IOError:
            print "Woa! Thats not a board."
    BOARDSIZE = len(board[0])


moves = {

'left': (-1,0),
'right': (1,0),
'up': (0,1),
'down':(0,-1),
'left and up': (-1,1),
'right and up': (1,1),
'left and down': (-1,-1),
'right and down':(1,-1)

}
toadCount = 4
steps = 0
def dist(p1, p2):
    return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)

def makeToad(i):
    toad = {}
    toad['id'] = i
    toad['x'] = BOARDSIZE
    toad['y'] = BOARDSIZE
    toad['distanceToMario'] = float('inf')
    toad['previousDistance'] = 0
    toad['direction'] = choice(moves.keys())
    return toad



mario = [0,0]
while True:
    mario = [choice(range(BOARDSIZE)),choice(range(BOARDSIZE))]
    if(board[mario[0]][mario[1]] is not boardUtils.wall):
        break
toads = [makeToad(i) for i in range(toadCount)]

def turn():
    board[mario[0]][mario[1]]=boardUtils.marioTrail
    move =  moves[choice(moves.keys())]
    dx = move[0]
    dy = move[1]
    print
    if not( board[mario[0] + dx][ mario[1] + dy]==boardUtils.wall):
        mario[0] += dx
        mario[1] += dy
    board[mario[0]][mario[1]]="M"
    for toad in toads:
        toad['previousDistance'] = toad['distanceToMario']
        toad['distanceToMario'] = dist(mario,[toad['x'],toad['y']])

        if toad['previousDistance'] < toad['distanceToMario']:
            toad['direction'] = choice(moves.keys())
        toadMove = moves[toad['direction']]

        board[toad['x']][toad['y']]=boardUtils.toadTrail
        if not( board[toad['x'] + toadMove[0]][ toad['y'] + toadMove[1]]==boardUtils.wall):
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
    sleep(.15)
    turn()
    steps += 1

    if checkCapture():
        break;



print "a toad found mario in",steps,"turns."
