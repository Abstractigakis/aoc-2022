import numpy as np

def numRightTrees(X, i, j):
    viewableTrees = 0
    for k in range(j+1, len(X[i])):
        viewableTrees += 1
        if X[i][k] >= X[i][j]:
            break
    return viewableTrees

def numLeftTrees(X, i, j):
    viewableTrees = 0
    for k in range(j-1, -1, -1):
        viewableTrees += 1
        if X[i][k] >= X[i][j]:
            break
    return viewableTrees

def numUpTrees(X, i, j):
    viewableTrees = 0
    for k in range(i-1, -1, -1):
        viewableTrees += 1
        if X[k][j] >= X[i][j]:
            break
    return viewableTrees

def numDownTrees(X, i, j):
    viewableTrees = 0
    for k in range(i+1, len(X)):
        viewableTrees += 1
        if X[k][j] >= X[i][j]:
            break
    return viewableTrees

def getSenicScore(X, i, j):
    return numRightTrees(X, i, j) * numLeftTrees(X, i, j) * numUpTrees(X, i, j) * numDownTrees(X, i, j)


with open("./data.txt") as f:
    X=np.array([ [int(i) for i in line.strip()] for line in f.readlines()])

    bestScore = 0
    for i in range(len(X)):
        for j in range(len(X[i])):
            bestScore = max(bestScore, getSenicScore(X, i, j))
    print(bestScore)
