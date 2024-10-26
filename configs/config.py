CONFIG = {
    'grid': [
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
    ], # you can change the grid here to test the algorithm with different mazes

    #17 is a perfect score for the maze
    'episodes': 200,
    'max_steps': 50,
    'alpha': 0.3, # learning rate
    'gamma': 0.9, # discount factor
    'epsilon': 1, # exploration

    'display_test_run': False, # display the final run after training with the visualizer
    'print_training_episode': False, #print the training episode number and total reward for the episode
    'print_data_summary': True
}
