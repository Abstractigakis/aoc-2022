with open("./data.txt") as f:
    p1,p2=0,0
    for line in f.readlines():
        m1, m2 = line[:-1].split(" ") 
        rps = ord(m1)-65
        ldw = ord(m2)-88
        p1 += rps + 1
        if ldw == 0:
            p1 += 6
            p2 += (rps - 1) %3 +1
        elif ldw == 1:
            p1 += 3
            p2 += 3 + rps + 1
        elif ldw == 2:
            p2 += (rps + 1) %3 +1
            p2 += 6
    print(p1, p2)
        