import math
from random import choice
from time import sleep

nextToadStep = {

'left': (-1,0),
'right': (1,0),
'up': (0,1),
'down':(0,-1)

}

marioMoves = [0]
toadMoves = nextToadStep.keys()

def dist(p1, p2):
    return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)

def makeToad():
    toad = {}
    toad['x'] = 0.0
    toad['y'] = 0
    toad['distanceToMario'] = float('inf')
    toad['previousDistance'] = 0
    toad['direction'] = choice(toadMoves)
    return toad




mario = [5.0,5.0]
toads = [makeToad() for i in range(1)]

def turn():

    for toad in toads:
        toad['previousDistance'] = toad['distanceToMario']
        toad['distanceToMario'] = dist(mario,[toad['x'],toad['y']])

        if toad['previousDistance'] < toad['distanceToMario']:
            toad['direction'] = choice(toadMoves)
        toadMove = nextToadStep[toad['direction']]
        toad['x'] += toadMove[0]
        toad['y'] += toadMove[1]
        print "toad moved",toad['direction']
        print "toad is now at",[toad['x'],toad['y']],"and",toad['distanceToMario'],"away from mario\n"




def checkWinner():
    capture = False
    for toad in toads:
        capture = capture or toad['x'] == mario[0] and toad['y'] == mario[1]
    return capture


print "mario is at",mario
while not checkWinner():

    sleep(.1)
    turn()


print "toads:",toads
print "Mario:",mario
