def fsort(s1):
    l2 = []
    d = dict()
    result = ""
    
    for i in range(len(s1)):
        d[s1[i]] = 0
    
    for i in range(len(s1)):
        d[s1[i]] += 1
        
    for i in (d):
        result = result + i
        result = result + str(d[i])
        
    
    # print (d)
    # print (result)
    return result
    


s1 = "abbaccc"
print(fsort(s1))
        