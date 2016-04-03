

grid = [[0,2,4,6,8],
[1,3,5,7,9]]


currentOutput = [(0,2,4,6,8),
(1,3,5,7,9)]

players = {'mario':{'pos':(0,1)},'toads':[{'pos':(2,3)},{'pos':(4,5)},{'pos':(6,7)},{'pos':(8,9)}]}

def gridToDict(grid):
    players = {}
    coords = zip(*grid)

    mario = {}
    mario['pos']=coords[0]

    toads = []
    for tup in coords[1:]:
        toad = {}
        toad['pos']=tup
        toads.append(toad)

    players['mario']=mario
    players['toads']=toads

    return players



def dictToGrid(players):
    tups = []
    mario = players['mario']['pos']
    tups.append(mario)
    for toad in players['toads']:
        tups.append(toad['pos'])

    grid = zip(*tups)


    return map(list,grid)

print players

print gridToDict(grid)

print "equal",players == gridToDict(grid)
