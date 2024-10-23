import numpy as np

from agents.dqn_agent import *
from configs.config import *
from maze.maze_environment import *
from utils.metrics import *
from utils.visualizer import *
from agents.q_learning_agent import *

def main():
    maze = Maze(CONFIG)

    #start a testing input loop that the user will use to temporarily replace the agent for debug
    #allow user to input w, a, s, d to give the move command to the maze with constant input loop
    reward = 0

    agent = Agent(maze, CONFIG)

    q_learning = QLearning(agent, maze)

    q_learning.train(CONFIG)

    q_learning.test(CONFIG)

if __name__ == '__main__':
    main()
