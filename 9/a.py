

with open("./data.txt") as f:
    H=0,0
    T=0,0
    seen=set()
    seen.add(T)
    for line in f.readlines():
        dir, dist=line.strip().split(" ")
        dist=int(dist)
        for i in range(dist):
            if dir == "R":
                H = H[0], H[1]-1
            elif dir == "L":
                H = H[0], H[1]+1
            elif dir == "U":
                H = H[0]+1, H[1]
            elif dir == "D":
                H = H[0]-1, H[1]

            dx = H[0] - T[0]
            dy = H[1] - T[1]

            if dx == 2 and dy == 1 or dx == 1 and dy == 2:
                T = T[0]+1, T[1]+1
            elif dx == -2 and dy == -1 or dx == -1 and dy == -2:
                T = T[0]-1, T[1]-1
            elif dx == -2 and dy == 1 or dx == -1 and dy == 2:
                T = T[0]-1, T[1]+1
            elif dx == 2 and dy == -1 or dx == 1 and dy == -2:
                T = T[0]+1, T[1]-1
            elif dx == 2 and dy == 0:
                T = T[0]+1, T[1]
            elif dx == 0 and dy == 2:
                T = T[0], T[1]+1
            elif dx == -2 and dy == 0:
                T = T[0]-1, T[1]
            elif dx == 0 and dy == -2:
                T = T[0], T[1]-1

            seen.add(T)

    print(seen)
    print(len(seen))