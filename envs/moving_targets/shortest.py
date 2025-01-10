import numpy as np
import itertools


"""
Use Floyd-Warshall to compute shortest distances between all states to compute optimal reward in expectation
"""
def shortest(N):
    # N-1 is the number of goal positions
    
    board = ['##########',
             '#        #',
             '#        #',
             '#    #   #',
             '#   ##   #',
             '#  ##    #',
             '#   #    #',
             '#        #',
             '#        #',
             '##########']

    arr = np.array([list(row) for row in board])
    free_spaces = list(map(tuple, np.argwhere(arr != '#')))

    dist = {(x, y) : np.inf for x in free_spaces for y in free_spaces}

    for (u, v) in dist.keys():
        d = abs(u[0] - v[0]) + abs(u[1] - v[1])
        if d == 0:
            dist[(u, v)] = 0
        elif d == 1:
            dist[(u, v)] = 1

    for k in free_spaces:
        for i in free_spaces:
            for j in free_spaces:
                if dist[(i, j)] > dist[(i, k)] + dist[(k, j)]:
                    dist[(i, j)] = dist[(i, k)] + dist[(k, j)]


    steps = []
    for points in itertools.combinations(free_spaces, N):
        distances = [dist[(points[0], points[i])] for i in range(1, N)]
        steps.append(np.min(distances))

    return np.mean(steps), np.std(steps)