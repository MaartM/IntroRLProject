
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

def get_maze():
    maze = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 'S', 1, 0, 0, 0, 1, 0, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
        [1, 1, 1, 0, 1, 1, 1, 1, 0, 1],
        [1, 0, 1, 'G', 0, 0, 0, 1, 0, 1],
        [1, 0, 0, 0, 1, 1, 0, 0, 0, 1],
        [1, 1, 1, 0, 1, 0, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 1, 'E', 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ]
    return maze

# Convert the maze into a numerical format for visualization
def convert_maze(maze):
    numerical_maze = np.zeros((len(maze), len(maze[0])), dtype=int)
    for y, row in enumerate(maze):
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
    return numerical_maze

def show_maze(maze):

    numerical_maze = convert_maze(maze)
    cmap = mcolors.ListedColormap(['white', 'black', 'green', 'blue', 'red'])
    bounds = [0, 1, 2, 3, 4, 5]  # Define the boundaries for the colors
    norm = mcolors.BoundaryNorm(bounds, cmap.N)
    
    plt.imshow(numerical_maze, cmap=cmap, norm=norm, interpolation='nearest')
    plt.xticks([])
    plt.yticks([])
    plt.title('Maze Representation')
    plt.show()
