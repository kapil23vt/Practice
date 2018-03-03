def fsort(s):
    result = ""
    helper = 1
    
    for i in range(len(s)-1):
        print(i)
        
        while(s[i] == s[i+1]):
            helper = helper + 1
        
        result += s[i]
        result += str(helper)
        
        helper = 1
    
    return (result)
            
s1 = "abcaa"
print(fsort(s1))
        