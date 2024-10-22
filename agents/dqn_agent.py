import numpy as np

class Agent:
    def __init__(self, maze, epsilon=0.1, alpha=0.1, gamma=0.9):
        self.maze = maze
        self.epsilon = epsilon
        self.alpha = alpha
        self.gamma = gamma
        self.action_space = [0, 1, 2, 3]
        self.state_space = len(self.maze.grid) * len(self.maze.grid[0])

    def choose_action(self, state, q_table):
        if np.random.uniform(0, 1) < self.epsilon:
            #print("exploring")
            return np.random.choice(self.action_space)
        else:
            #print("exploiting")
            return np.argmax(q_table[state])
