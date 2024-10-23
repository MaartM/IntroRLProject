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
    ],

    #at 100 episodes with 100 max steps, the algorirthm will complete the maze sometimes, but not all the time. at 1000 for both, it is relatively consistent.
    #17 is a perfect score for the maze
    'episodes': 1000,
    'max_steps': 1000,
    'alpha': 0.5,
    'gamma': 0.9,
    'epsilon': 1,

    'display_test_run': True, # display the final run after training with the visualizer
    'print_training_episode': False, #print the training episode number and total reward for the episode
    'print_data_summary': True
}
