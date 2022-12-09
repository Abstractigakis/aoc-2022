
def calcNextPos(H, T):
    dx = H[0] - T[0]
    dy = H[1] - T[1]

    if dx == 2 and dy > 0 or dx > 0 and dy == 2:
        T = T[0]+1, T[1]+1
    elif dx == -2 and dy < 0 or dx < 0 and dy == -2:
        T = T[0]-1, T[1]-1
    elif dx == -2 and dy > 0 or dx < 0 and dy == 2:
        T = T[0]-1, T[1]+1
    elif dx == 2 and dy < 0 or dx > 0 and dy == -2:
        T = T[0]+1, T[1]-1

    elif dx == 2 and dy == 0:
        T = T[0]+1, T[1]
    elif dx == 0 and dy == 2:
        T = T[0], T[1]+1
    elif dx == -2 and dy == 0:
        T = T[0]-1, T[1]
    elif dx == 0 and dy == -2:
        T = T[0], T[1]-1

    return T

with open("./data.txt") as f:
    posArr =[(0,0)]*10

    seen=set()
    seen.add(posArr[len(posArr)-1])

    for line in f.readlines():
        dir, dist=line.strip().split(" ")
        dist=int(dist)

        for _ in range(dist):
            if dir == "R":
                posArr[0] = posArr[0][0], posArr[0][1]-1
            elif dir == "L":
                posArr[0] = posArr[0][0], posArr[0][1]+1
            elif dir == "U":
                posArr[0] = posArr[0][0]+1, posArr[0][1]
            elif dir == "D":
                posArr[0] = posArr[0][0]-1, posArr[0][1]

            for j in range(1, len(posArr)):
                posArr[j] = calcNextPos(posArr[j-1], posArr[j])
            seen.add(posArr[len(posArr)-1])

    print(seen)
    print(len(seen))