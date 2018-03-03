def sequencemicro(l1):
    l2 = []
    for i in range(len(l1)):
        if l1[i] > 0:
            l2.append(l1[i])
            
    for i in range(len(l1)):
        if l1[i] < 0:
            l2.append(l1[i])
    
    for i in range(len(l1)):
        if l1[i] == 0:
            l2.append(l1[i])
    return l2


l1 = [1,-1,2,-3,0]
print(sequencemicro(l1))
        