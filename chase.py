import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

def gridToDict(grid):
    players = {}

    mario = {}
    mario['pos']=(grid[0][0],grid[0][1])

    toads = []
    toads.append({'pos':(grid[0][2],grid[0][3])})
    toads.append({'pos':(grid[0][4],grid[1][0])})
    toads.append({'pos':(grid[1][1],grid[1][2])})
    toads.append({'pos':(grid[1][3],grid[1][4])})

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

# takes a dict of all players (mario plus four toads) and returns mario's new coordinates
def moveMario(players):

    mario = players['mario']
    current = list(mario['pos'])
    dxy = np.random.random(2) * .2
    dxy -= .05

    newPosition = [x + y for x, y in zip(current,dxy)]

    players['mario']['pos'] = tuple(newPosition)

    return players['mario']

#takes a toad, returns a new toad after it has been moved.
def moveToad(toad):

    return toad

def processFrame(grid):
    players = gridToDict(grid)

    mario = players['mario']
    toads = players['toads']

    players['mario'] = moveMario(players)


    movedToads = []
    for toad in players['toads']:
        movedToads.append(moveToad(toad))
    players['toads'] =  movedToads
    grid = dictToGrid(players)

    return grid

def transposeGrid(grid):
    newGrid = np.zeros((2,5))
    newGrid[0][0] = grid[0][0]
    newGrid[1][0] = grid[0][1]

    newGrid[0][1] = grid[0][2]
    newGrid[1][1] = grid[0][3]

    newGrid[0][2] = grid[0][4]
    newGrid[1][2] = grid[1][0]

    newGrid[0][3] = grid[1][1]
    newGrid[1][3] = grid[1][2]

    newGrid[0][4] = grid[1][3]
    newGrid[1][4] = grid[1][4]

    return newGrid

class AnimatedScatter(object):
    """An animated scatter plot using matplotlib.animations.FuncAnimation."""
    def __init__(self, numpoints=2):
        self.numpoints = numpoints
        self.stream = self.data_stream()

        # Setup the figure and axes...
        self.fig, self.ax = plt.subplots() # what are these spicifically?
        # Then setup FuncAnimation. check out http://matplotlib.org/api/animation_api.html
        self.ani = animation.FuncAnimation(self.fig, self.update, interval=5,
                                           init_func=self.setup_plot, blit=True)

    def setup_plot(self):
        """Initial drawing of the scatter plot."""
        x, y, s, c = next(self.stream)
        self.scat = self.ax.scatter(x, y, c=c, s=s, animated=True)
        self.ax.axis([-10, 10, -10, 10])

        # For FuncAnimation's sake, we need to return the artist we'll be using
        # Note that it expects a sequence of artists, thus the trailing comma.
        return self.scat,

    def data_stream(self): # assume first list is mario, rest are toad.
        """Generate a random walk (brownian motion). Data is scaled to produce
        a soft "flickering" effect.

        s: size
        c: color
        xy: list of list representing location of the points.

        """
        data = np.random.random((4, self.numpoints)) # found problem
        xy = data[:2, :]
        print "xy:",xy
        s, c = data[2:, :]
        print "s:",s
        print "c:",c

        xy -= 0.5
        xy *= 10
        while True:

            """print data
            #mario
            xy[0][0] += .03
            xy[0][1] += -.23
            s += 0.05 * (np.random.random(self.numpoints) - 0.5)
            c += 0.02 * (np.random.random(self.numpoints) - 0.5)"""

            grid = data[:2, :]

            mario = grid[0]
            toad = grid[1]


            grid[0] = moveMario(mario)
            grid[1] = moveToad(distanceToMario)






            yield data

    def update(self, i):
        """Update the scatter plot."""
        data = next(self.stream)
        # Set x and y data...
        self.scat.set_offsets(data[:2, :])
        # Set sizes...
        self.scat._sizes = 300 * abs(data[2])**1.5 + 100
        # Set colors..
        self.scat.set_array(data[3])

        # We need to return the updated artist for FuncAnimation to draw..
        # Note that it expects a sequence of artists, thus the trailing comma.
        return self.scat,

    def show(self):
        ani = self.ani
        ani.save('scatter.gif', writer='imagemagick', fps=12);
if __name__ == '__main__':
    a = AnimatedScatter()
    a.show()
