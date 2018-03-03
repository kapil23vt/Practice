def searchsub(s1, s2):
      
    l1 = len(s1)
    l2 = len(s2)

    for i in range(l1):
        
        if s1[i] == s2[0] and l2 == 1:
            return True

            # found the first matching character
            # check next (l2-1) characters
        
        if s1[i] == s2[0] and l2 > 1:
            
            # Comparing next (l2-1) elements    
            for j in range(l2-1):
                                
                if s1[i+j+1] != s2[j+1]:
                    return False
            
            return True
s1 = 'kapilkale'
s2 = 'apilg'
print(searchsub(s1, s2))