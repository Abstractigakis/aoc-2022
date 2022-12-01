with open("./data.txt") as f:
    calsArr = []
    currCals = 0
    for line in f.readlines():
        if line == '\n':
            calsArr.append(currCals)
            currCals=0
        else:
            currCals += int(line)
    print(max(calsArr))