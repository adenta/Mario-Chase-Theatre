import boardUtils, math
from random import choice

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

def dist(p1, p2):
    return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)


def mario2(mario,toads,board):
            closestToad = 0
            for toad in toads:
                if dist(mario,[toad['x'],toad['y']]) > closestToad:
                    closestToad = toad

            xdiff = mario[0]-closestToad['x']
            ydiff = mario[1]-closestToad['y']
            if abs(xdiff) < abs(ydiff):
                if xdiff > 0:
                    dx = 1
                    dy = 0
                else:
                    dx = -1
                    dy = 0
            elif abs(ydiff) < abs(xdiff):
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

            return mario

def toad2(mario,toads,board):
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

    return toads
