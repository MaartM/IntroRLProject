## don't worry about me just trying to generate a random 10x10 maze

import random

def generate_simple_maze(height, width):
    # Initialize the maze with walls (1 for wall, 0 for passage)
    maze = [[1 for _ in range(width)] for _ in range(height)]

    # Randomly create passages while ensuring they are connected
    for i in range(1, height, 2):
        for j in range(1, width, 2):
            maze[i][j] = 0  # Create a passage
            # Randomly connect to an adjacent cell
            if i > 1 and random.choice([True, False]):
                maze[i-1][j] = 0  # Connect to the cell above
            if j > 1 and random.choice([True, False]):
                maze[i][j-1] = 0  # Connect to the cell on the left

    # Ensure the outer walls remain
    for i in range(height):
        maze[i][0] = maze[i][width-1] = 1
    for j in range(width):
        maze[0][j] = maze[height-1][j] = 1

    return maze

def print_maze(maze):
    for row in maze:
        print(''.join(['#' if cell == 1 else ' ' for cell in row]))

# Example usage:
height = 10  # Can be even
width = 10   # Can be even
maze = generate_simple_maze(height, width)
print_maze(maze)
