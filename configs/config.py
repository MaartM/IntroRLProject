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
    'start': (1, 1),
    'goal': (7, 8),
    'subgoal': (3, 5),

    #at 100 episodes, the algorirthm will complete the maze sometimes, but not all the time. at 1000, it is relatively consistent.
    'episodes': 1000,
    'max_steps': 1000,
    'alpha': 0.5,
    'gamma': 0.9,
    'epsilon': 1
}
