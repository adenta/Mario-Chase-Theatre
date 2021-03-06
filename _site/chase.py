import math, boardUtils, io, copy, json, yaml, time, behavior
from random import choice
from time import sleep

inputFlag = True
defaultBoard = "blank.txt"
boardName = None
if inputFlag:

    while True:
        userBoard = raw_input("What board do you want to use? ") + ".txt"
        boardName = userBoard[:-4]
        try:
            board = boardUtils.readBoard(userBoard)
            break
        except IOError:
            print "Woa! Thats not a board."
else:
    board = boardUtils.readBoard(defaultBoard)

initBoard = copy.deepcopy(board)

BOARDSIZE = int((len(board[0])+1)/float(2))



def dist(p1, p2):
    return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)

def makeToad(i):
    toad = {}
    toad['id'] = i
    toad['x'] = BOARDSIZE
    toad['y'] = BOARDSIZE
    toad['distanceToMario'] = float('inf')
    toad['previousDistance'] = 0
    toad['direction'] = choice(behavior.moves.keys())
    return toad



def trial(toadCount, timer,delay,marioBehavior,toadBehavior):
    board = copy.deepcopy(initBoard)
    steps = 0
    mario = [0,0]
    frames = []
    currentTime = time.strftime("%Y%m%d-%H%M%S")

    match = {}
    match['id'] = currentTime
    match['timer'] = timer
    match['toads'] = toadCount
    match['marioBehavior'] = marioBehavior
    match['toadBehavior'] = toadBehavior
    match['map'] = boardUtils.jsonBoard(initBoard)
    frames = []


    while True:
        mario = [choice(range(BOARDSIZE)),choice(range(BOARDSIZE))]
        if(board[mario[0]][mario[1]] is not boardUtils.wall):
            break
    toads = [makeToad(i) for i in range(toadCount)]

    def drawTime():
        remaining = timer - steps
        minutes = str(remaining // 60)
        seconds = str(remaining % 60)
        return minutes + ":" + seconds + "."

    def makeActor(x,y,typ):
        actor = {}
        actor['x'] = x
        actor['y'] = y
        actor['type'] = typ

        return  actor
    def makeFrame(mario,toads):
        frame = {}
        points = []
        frame['step'] = steps
        points.append(makeActor(mario[0],mario[1],"mario"))
        for toad in toads:
            points.append(makeActor(toad['x'],toad['y'],"toad"))
        frame['points'] = points
        return frame



    def turn():
        board[mario[0]][mario[1]]=boardUtils.marioTrail
        #Mario AI

        newMario = behavior.mario(mario,toads,board,marioBehavior)
        board[newMario[0]][newMario[1]]=boardUtils.mario

        #Toad AI
        newToads = behavior.toad(mario,toads,board,toadBehavior)
        for toad in newToads:
            board[toad['x']][toad['y']]=boardUtils.toad
            if delay is not 0:
                print "toad moved",toad['direction']
                print "toad",toad['id'],"is now at",[toad['x'],toad['y']],"and",toad['distanceToMario'],"away from mario,",mario,"\n"
        if delay is not 0:
            print "Time:",drawTime()
            boardUtils.drawBoard(board)
        return makeFrame(mario,toads)


    def checkCapture():
        capture = False
        for toad in toads:
            capture = capture or toad['x'] == mario[0] and toad['y'] == mario[1]
        return capture


    while True:

        sleep(delay)
        frames.append(turn())
        steps += 1

        if checkCapture():
            if delay is not 0:
                print "a toad found mario in",steps,"turns."
            isCaptured = True
            break;

        if steps >= timer:
            if delay is not 0:
                print "Mario wins!"
            isCaptured = False
            break
    match['frames'] = frames
    jsonOut = open("./data/" + boardName + "_M-" + str(marioBehavior) + "_T-" + str(toadBehavior) + "-" + currentTime + ".json",'w')
    jsonOut.write(json.dumps(match,indent=4))


    return (isCaptured,steps)
