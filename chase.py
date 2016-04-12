import math, boardUtils, io
from random import choice
from time import sleep

inputFlag = True
defaultBoard = "blank.txt"
if inputFlag:

    while True:
        userBoard = raw_input("What board do you want to use? ") + ".txt"
        try:
            board = boardUtils.readBoard(userBoard)
            break
        except IOError:
            print "Woa! Thats not a board."
else:
    board = boardUtils.readBoard(defaultBoard)

BOARDSIZE = int((len(board[0])+1)/float(2))

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
    #Mario AI
    closestToad = 0
    for toad in toads:
        if dist(mario,[toad['x'],toad['y']]) > closestToad:
            closestToad = toad
    #print closestToad['x']
    #print closestToad['y']
    #print dist(mario,[closestToad['x'],closestToad['y']])
    xdiff = mario[0]-closestToad['x']
    ydiff = mario[1]-closestToad['y']
    if abs(xdiff) < abs(ydiff):
        if xdiff > 0:
            dx = 1
            dy = 0
        else:
            dx = -1
            dy = 0
    elif ydiff > xdiff:
        if ydiff > 0:
            dy = 1
            dx = 0 
        else:
            dy = -1
            dx = 0
    else:
        move =  moves[choice(moves.keys())]
        dx = move[0]
        dy = move[1]
    while True:
        if not( board[mario[0] + dx][ mario[1] + dy]==boardUtils.wall):
            mario[0] += dx
            mario[1] += dy
            break
        move =  moves[choice(moves.keys())]
        dx = move[0]
        dy = move[1]
        
    board[mario[0]][mario[1]]=boardUtils.mario
    
    #Toad AI
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

        board[toad['x']][toad['y']]=boardUtils.toad

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
