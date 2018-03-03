def fsort(s1):
    l2 = []
    d = dict()
    result = ""
    
    for i in range(len(s1)):
        d[s1[i]] = 0
    
    for i in range(len(s1)):
        d[s1[i]] += 1
        
    print (d)
    
    for i in d:
        if d[i] < 3:
            for j in range(d[i]):
                result = result + i

    return result
    


s1 = "abbbccc"
print(fsort(s1))
        