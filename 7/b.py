import pprint

with open("./data.txt") as f:
    dirs={
        'home':0,
    }
    path=['home']
    for line in f.readlines():
        args = line[:-1].split(" ")
        if args[0] == "$" and args[1] == "cd" and args[2] == "..":
            path = path[:-1]
        elif args[0] == "$" and args[1] == "cd" and args[2] == "/":
            path=['home']
        elif args[0] == "$" and args[1] == "cd":
            path.append(args[2])
        elif args[0] == "$" and args[1] == "ls":
            continue


        try:
            size=int(args[0])
        except:
            continue
        
        for i, dir in enumerate(path):
            currPath = "/".join(path[:i+1])
            try:
                dirs[currPath] += size
            except:
                dirs[currPath] = size
            

    pprint.pprint(dirs)
    totalUsedSpace = dirs['home']
    spaceRequired = 30000000
    diskSpace = 70000000
    remainingSpace = diskSpace - totalUsedSpace

    currDirToDelete = 'home'
    currSmallestSpaceToReclaim = diskSpace
    for dir in dirs:
        deletedFileSpace = dirs[dir]
        if remainingSpace + deletedFileSpace >= spaceRequired and deletedFileSpace < currSmallestSpaceToReclaim:
            currSmallestSpaceToReclaim = deletedFileSpace
            currDirToDelete = dir

    print(currDirToDelete, currSmallestSpaceToReclaim)

