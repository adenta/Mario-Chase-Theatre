import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()
points, = ax.plot(np.random.rand(10), 'o')
ax.set_ylim(-.5, .5)
ax.set_xlim(-10, 10)

def update(data):
    points.set_ydata(data)
    return points,

def generate_points():
    while True:
        yield np.random.rand(10)-.5  # change this

ani = animation.FuncAnimation(fig, update, generate_points, interval=100)
ani.save('animation.gif', writer='imagemagick', fps=12);
