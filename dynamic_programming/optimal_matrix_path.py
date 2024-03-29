"""
We are given an nxm matrix.
The elements in the matrix are random, positive integers.
We want to go from the top left corner to the bottom right
by moving only right and down (no left, up or diagonal moves).
Our goal is to move using the minimum cost path.

f(i, j) = min{ f(i-1, j), f(i, j-1) } + matrix(i, j)
"""

import numpy as np
matrix = [[5, 3, 10, 17, 1],
          [4, 2, 9, 8, 5],
          [11, 12, 3, 9, 6],
          [1, 3, 4, 2, 10]]

matrix = np.matrix(matrix)

def optimal_path(n, m):
    solutions = np.matrix([[-1 for i in range(m)] for j in range(n)])
    path = [[(-1, -1) for i in range(m)] for j in range(n)]
    
    solutions[0, 0], path[0][0] = matrix[0, 0], (0, 0)
    
    # initialize left column
    for i in range(1, n):
        solutions[i, 0] = solutions[i-1, 0] + matrix[i, 0]
        path[i][0] = (i-1, 0)
    
    # initialize top row
    for j in range(1, m):
        solutions[0, j] = solutions[0, j-1] + matrix[0, j]
        path[0][j] = (0, j-1)
    
    # build rest
    for i in range(1, n):
        for j in range(1, m):
            if solutions[i-1, j] < solutions[i, j-1]:
                # choose right
                solutions[i, j] = solutions[i-1, j] + matrix[i, j]
                path[i][j] = (i-1, j)
            else:
                # choose down
                solutions[i, j] = solutions[i, j-1] + matrix[i, j]
                path[i][j] = (i, j-1)
    
    print(solutions)
    
    p = path[-1][-1]
    print(p)
    while True:
        p = path[p[0]][p[1]]
        print(p)
        if p == (0, 0): break

optimal_path(matrix.shape[0], matrix.shape[1])
