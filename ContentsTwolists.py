def comparelists(l1,l2):
    len1 = len(l1)
    len2 = len(l2)
    
    result = 0
    d = dict()
    for i in range(len(l2)):
        d[l2[i]] = i 
    
    print (d)
    for i in range(len(l1)):
        key = l1[i]
        
        if key in d:
            result+=1
    
    if (result == len(l1) and result == len(l2)):
        return True
    else:
        return False

l1 = [1,1,2,2]
l2 = [1,1,1,2]
print(comparelists(l1, l2))
        