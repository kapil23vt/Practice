def unique(s):
    d = dict()
    
    for i in range(len(s)):
        d[s[i]] = 0
    
    for i in range(len(s)):
        d[s[i]] += 1
    
    print(d)
    
    if (len(s) == len(d)):
        return True
    else:
        return False

s = 'xyzw' #prints False
print(unique(s))