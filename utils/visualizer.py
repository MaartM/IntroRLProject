import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

def show_maze(maze, input):

    numerical_maze = convert_maze(maze)

    cmap = mcolors.ListedColormap(['white', 'black', 'green', 'blue', 'red'])
    bounds = [0, 1, 2, 3, 4, 5]
    norm = mcolors.BoundaryNorm(bounds, cmap.N)
    
    plt.clf()
    plt.imshow(numerical_maze, cmap=cmap, norm=norm, interpolation='nearest')

    plt.xticks([])
    plt.yticks([])

    plt.title('Input: ' + input)

    plt.pause(0.2)
    if maze.is_done():
        plt.pause(4)

def convert_maze(maze):
    numerical_maze = np.zeros((len(maze.grid), len(maze.grid[0])), dtype=int)
    for y, row in enumerate(maze.grid):
        for x, cell in enumerate(row):
            if cell == 1:
                numerical_maze[y, x] = 1
            elif cell == 0:
                numerical_maze[y, x] = 0
            elif cell == 'S':
                numerical_maze[y, x] = 2
            elif cell == 'G':
                numerical_maze[y, x] = 3
            elif cell == 'E':
                numerical_maze[y, x] = 4
    x, y = maze.current_position
    numerical_maze[y, x] = 2
    return numerical_maze

def convert_input(action):
    if action == 0:
        return 'w'
    if action == 1:
        return 'a'
    if action == 2:
        return 's'
    if action == 3:
        return 'd'
