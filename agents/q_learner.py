import numpy as np
from utils.visualizer import *

class QLearning:
    def __init__(self, agent, maze):
        self.agent = agent
        self.maze = maze
        self.q_table = np.zeros((self.agent.state_space, len(self.agent.action_space)))


    def train(self, config):
        episodes = config['episodes']

        self.first_finished_run = 0
        self.first_perfect_run = 0
        self.average_reward = 0
        self.number_of_perfect_runs = 0
        self.average_score_first_fifth = 0
        self.average_score_last_fifth = 0

        for episode in range(episodes):
            self.maze.reset()
            state = (self.maze.current_position[0] - 1) * len(self.maze.grid[0]) + self.maze.current_position[1]
            endreached = False
            total_reward = 0

            while not self.maze.is_done():
                action = self.agent.choose_action(state, self.q_table)
                next_state = self.maze.move(action)
                next_state = (next_state[0] - 1) * len(self.maze.grid[0]) + next_state[1]
                reward = self.maze.get_reward()
                total_reward += reward
                self.q_table[state][action] += self.agent.alpha * (reward + self.agent.gamma * np.max(self.q_table[next_state]) - self.q_table[state][action])
                state = next_state

            if config['print_training_episode']:
                print("Episode: ", episode, " Reward: ", total_reward, " Epsilon: ", self.agent.epsilon)

            if config['print_data_summary']:
                if total_reward == 17:
                    self.number_of_perfect_runs += 1
                    if self.first_perfect_run == 0:
                        self.first_perfect_run = episode
                if total_reward > (config['max_steps'] - 10) * -1 and self.first_finished_run == 0:
                    self.first_finished_run = episode
                self.average_reward += total_reward
                if episode < episodes / 5:
                    self.average_score_first_fifth += total_reward
                if episode > episodes - episodes / 5:
                    self.average_score_last_fifth += total_reward


            self.agent.decay_epsilon()
        
        if config['print_data_summary']:
            print("Average Reward: ", self.average_reward / episodes)
            print("Number of Perfect Runs: ", self.number_of_perfect_runs)
            print("Average Score First Fifth: ", self.average_score_first_fifth / (episodes / 5))
            print("Average Score Last Fifth: ", self.average_score_last_fifth / (episodes / 5))
            print("First Finished Run: ", self.first_finished_run)
            print("First Perfect Run: ", self.first_perfect_run)

    def test(self, config):
        self.maze.reset()
        state = (self.maze.current_position[0] - 1) * len(self.maze.grid[0]) + self.maze.current_position[1]
        endreached = False
        total_reward = 0
        show_n = 0
        while not self.maze.is_done():
            if show_n < 20 and config['display_test_run']:
                show_maze(self.maze)
                show_n += 1
            action = np.argmax(self.q_table[state])
            next_state = self.maze.move(action)
            next_state = (next_state[0] - 1) * len(self.maze.grid[0]) + next_state[1]
            reward = self.maze.get_reward()
            total_reward += reward
            state = next_state
        if total_reward <= (config['max_steps'] - 10) * -1:
            print("Failed to reach goal")
        else:
            print("Final run Reward: ", total_reward)
            if total_reward == 17:
                print("Optimal Run: Yes")
            else:
                print("Optimal Run: No")
