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
        else:
            result = result + i + str(d[i])

    return result
    


s1 = "abbbccc" #output should be aab3c3d
print(fsort(s1))
        