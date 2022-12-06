with open('data.txt') as f:
    fcp=0
    for line in f.readlines():
        line=line[:-1]
        i1,i2=line.split(",")
        a,b=i1.split("-")
        x,y=i2.split("-")

        x=int(x)
        y=int(y)
        a=int(a)
        b=int(b) 
        
        if not(x>b and y>b or x<a and y<a): 
            fcp+=1
    print(fcp)