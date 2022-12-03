def getPiro(c:str):
    return ord(c)-97 if c.islower() else ord(c)-65+26
    

with open("./data.txt") as f:
    sum = 0 
    for line in f.readlines():
        line = line[:-1]
        
        comp1, comp2=line[:len(line)//2], line[len(line)//2:]
        
        numLetters =26*2
        counts1 = [0] * (numLetters)
        counts2 = [0] * (numLetters)

        for c in comp1:
            counts1[getPiro(c)] += 1
        for c in comp2:
            counts2[getPiro(c)] += 1
            
        for i in range(numLetters):  
            if counts1[i]>0 and counts2[i]>0:
                sum += i + 1
                break
    print(sum)

        

