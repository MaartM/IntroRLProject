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

    'episodes': 1000,
    'max_steps': 1000,
    'alpha': 0.1,
    'gamma': 0.6,
    'epsilon': 0.1
}
