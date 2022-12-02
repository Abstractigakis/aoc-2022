with open("./data.txt") as f:
    p1,p2=0,0
    loss, draw, win = 0,3,6
    r, p, s = 1,2,3
    matrix=[
        [(draw+r,draw+r),   (loss+r,win+p), (win+r,loss+s)],
        [(win+p,loss+r),    (draw+p,draw+p),(loss+p,win+s)],
        [(loss+s,win+r),    (win+s,loss+p), (draw+s,draw+s)],
    ]

    for line in f.readlines():
        m1, m2 = line[:-1].split(" ")
        p1 += matrix[ord(m1)-65][ord(m2)-88][0]
        p2 += matrix[ord(m1)-65][ord(m2)-88][1]
    print(p1, p2)
        