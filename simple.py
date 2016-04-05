import math
from random import choice
from time import sleep

nextToadStep = {

'left': (-1,0),
'right': (1,0),
'up': (0,1),
'down':(0,-1),
'left and up': (-.5,.5),
'right and up': (.5,.5),
'left and down': (-.5,-.5),
'right and down':(.5,-.5)

}

toadCount = 4
steps = 0
marioMoves = [0.5,-0.5]
toadMoves = nextToadStep.keys()
boardSize = 100
def dist(p1, p2):
    return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)

def makeToad(i):
    toad = {}
    toad['id'] = i
    toad['x'] = 0.0
    toad['y'] = 0
    toad['distanceToMario'] = float('inf')
    toad['previousDistance'] = 0
    toad['direction'] = choice(toadMoves)
    return toad




mario = [choice(range((-1* (boardSize/2)),boardSize/2)),choice(range((-1* (boardSize/2)),boardSize/2))]
toads = [makeToad(i) for i in range(toadCount)]

def turn():
    mario[0] += choice(marioMoves)
    mario[1] += choice(marioMoves)

    for toad in toads:
        toad['previousDistance'] = toad['distanceToMario']
        toad['distanceToMario'] = dist(mario,[toad['x'],toad['y']])

        if toad['previousDistance'] < toad['distanceToMario']:
            toad['direction'] = choice(toadMoves)
        toadMove = nextToadStep[toad['direction']]
        toad['x'] += toadMove[0]
        toad['y'] += toadMove[1]
        print "toad moved",toad['direction']
        print "toad",toad['id'],"is now at",[toad['x'],toad['y']],"and",toad['distanceToMario'],"away from mario,",mario,"\n"




def checkCapture():
    capture = False
    for toad in toads:
        capture = capture or toad['x'] == mario[0] and toad['y'] == mario[1]
    return capture



print "mario is at",mario
while True:
    turn()
    steps += 1

    if checkCapture():
        break;



print "a toad found mario in",steps,"turns."
