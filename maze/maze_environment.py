class Maze:
    def __init__(self, grid, start, goal, subgoal):
        self.grid = grid
        self.start = start
        self.goal = goal
        self.subgoal = subgoal
        self.current_position = start
        self.subgoal_reached = False

    def reset(self):
        self.current_position = self.start
        return self.start

    def move(self, action):
        x, y = self.current_position
        #1234 are w a s d in order
        if action == 0:
            y -= 1
        elif action == 1:
            x -= 1
        elif action == 2:
            y += 1
        elif action == 3:
            x += 1
        if self.grid[y][x] == 1:
            return self.current_position
        else:
            self.current_position = (x, y)
            return self.current_position

    def get_reward(self):
        if self.current_position == self.goal:
            if self.subgoal_reached:
                return 20
        elif self.current_position == self.subgoal and not self.subgoal_reached:
            self.subgoal_reached = True
            return 10
        else:
            return -1

    def step(self, action):
        new_position = self.move(action)
        reward = self.get_reward()
        return new_position, reward

    def is_done(self):
        return self.current_position == self.goal
