import numpy as np

class QLearning:
    def __init__(self, agent, maze):
        self.agent = agent
        self.maze = maze
        self.q_table = np.zeros((self.agent.state_space, len(self.agent.action_space)))


    def train(self, config):
        episodes = config['episodes']
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
            print("Episode: ", episode, " Reward: ", total_reward)
            self.agent.decay_epsilon()

    def test(self):
        self.maze.reset()
        state = (self.maze.current_position[0] - 1) * len(self.maze.grid[0]) + self.maze.current_position[1]
        endreached = False
        total_reward = 0
        while not self.maze.is_done():
            action = np.argmax(self.q_table[state])
            print("Action: ", action)
            next_state = self.maze.move(action)
            next_state = (next_state[0] - 1) * len(self.maze.grid[0]) + next_state[1]
            reward = self.maze.get_reward()
            total_reward += reward
            state = next_state
        if total_reward < -1000:
            print("Failed to reach goal")
        else:
            print("Test Reward: ", total_reward)
