import numpy as np

from agents.agent import *
from configs.config import *
from maze.maze import *
from utils.metrics import *
from utils.visualizer import *
from agents.q_learner import *

def main():
    maze = Maze(CONFIG)
    agent = Agent(maze, CONFIG)
    q_learning = QLearning(agent, maze)
    q_learning.train(CONFIG)
    q_learning.test(CONFIG)

if __name__ == '__main__':
    main()
