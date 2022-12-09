import numpy as np

def checkVisibleTreesFromLeft(X):
    visibleTrees = set()
    for i in range(len(X)):
        tallestTree = -1
        for j in range(len(X[i])):
            if X[i][j] > tallestTree:
                tallestTree = X[i][j]
                visibleTrees.add((i,j))
    return visibleTrees

def checkVisibleTreesFromRight(X):
    visibleTrees = set()
    for i in range(len(X)):
        tallestTree = -1
        for j in range(len(X[i])-1,0,-1):
            if X[i][j] > tallestTree:
                tallestTree = X[i][j]
                visibleTrees.add((i,j))
    return visibleTrees


def checkVisibleTreesFromTop(X):
    visibleTrees = set()
    for j in range(len(X[0])):
        tallestTree = -1
        for i in range(len(X)):
            if X[i][j] > tallestTree:
                tallestTree = X[i][j]
                visibleTrees.add((i,j))
    return visibleTrees

def checkVisibleTreesFromBottom(X):
    visibleTrees = set()
    for j in range(len(X[0])):
        tallestTree = -1
        for i in range(len(X)-1,0,-1):
            if X[i][j] > tallestTree:
                tallestTree = X[i][j]
                visibleTrees.add((i,j))
    return visibleTrees


with open("./data.txt") as f:
    X=np.array([ [int(i) for i in line.strip()] for line in f.readlines()])

    visibleTreesLeft = checkVisibleTreesFromLeft(X)
    visibleTreesRight = checkVisibleTreesFromRight(X)
    visibleTreesTop = checkVisibleTreesFromTop(X)
    visibleTreesBottom = checkVisibleTreesFromBottom(X)

    visibleTrees = visibleTreesLeft.union(visibleTreesTop).union(visibleTreesRight).union(visibleTreesBottom)
    print(len(visibleTrees))
