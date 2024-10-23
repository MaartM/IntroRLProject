import numpy as np

class Agent:
    def __init__(self, maze, config):
        self.maze = maze
        self.epsilon = config['epsilon']
        self.alpha = config['alpha']
        self.gamma = config['gamma']
        self.action_space = [0, 1, 2, 3]
        self.state_space = len(self.maze.grid) * len(self.maze.grid[0])

    def choose_action(self, state, q_table):
        if np.random.uniform(0, 1) < self.epsilon:
            return np.random.choice(self.action_space)
        else:
            return np.argmax(q_table[state])

    def decay_epsilon(self):
        self.epsilon = self.epsilon * 0.99
