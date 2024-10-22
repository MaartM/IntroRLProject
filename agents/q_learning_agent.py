import numpy as np

class QLearning:
    def __init__(self, agent, maze):
        self.agent = agent
        self.maze = maze
        self.q_table = np.zeros((self.agent.state_space, len(self.agent.action_space)))

    def train(self, episodes):
        for episode in range(episodes):
            self.maze.reset()
            state = self.maze.current_position
            while not self.maze.is_done():
                action = self.agent.choose_action(state, self.q_table)
                next_state = self.maze.move(action)
                reward = self.maze.get_reward()
                self.q_table[state][action] += self.agent.alpha * (reward + self.agent.gamma * np.max(self.q_table[next_state]) - self.q_table[state][action])
                state = next_state
            print("Episode: ", episode, " Reward: ", reward)

    def test(self):
        self.maze.reset()
        state = self.maze.current_position
        while not self.maze.is_done():
            action = self.agent.choose_action(state, self.q_table)
            next_state = self.maze.move(action)
            self.maze.get_reward()
            state = next_state
        self.maze.reset()
        print("Test complete")
