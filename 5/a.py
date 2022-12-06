with open('data.txt') as f:
    stacks = [
        "HLRFBCJM",
        "DCZ",
        "WGNCFJH",
        "BSTMDJP",
        "JRDCN",
        "ZGJPQDLW",
        "HRFTZP",
        "GMVL",
        "JRQFPGBC"
    ]
    print(stacks)
    for i in range(len(stacks)):
        stacks[i]=stacks[i][::-1]
    for line in f.readlines()[10:]:
        line = line[:-1]
        s = line.split(" ")
        n = int(s[1])
        f = int(s[3])
        t = int(s[5])
        print(s,n,f,t) 
        stacks[t-1] += stacks[f-1][-n:][::-1]
        stacks[f-1] = stacks[f-1][:-n]
        print(stacks)
    res = ""
    for s in stacks:
        res +=s[-1]
    print(res)