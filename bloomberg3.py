

def boom(s1, start, helper):
    
    end = len(s1) - 1
    #print(end)
    
    for i in range(1, len(s1)-1):
        
        while(s1[start] == s1[helper]):
            helper = helper + 1
        
    if (helper - start) >= 2:
        start = helper + 1
        
    #print(start)
    #print(helper)
    
    #return string from (start-1) to end
    
    tempanswer = str(s1[start-1:len(s1)])
    # tempanswer = str()
    
    if tempanswer == s1:
        return tempanswer
    else:
        boom(tempanswer, start, start+1)
    


s1 = raw_input("aaabbb") #output should be aab3c3d
print(boom(s1,0,1)       