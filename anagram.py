def anagram(l1,l2):
    
    d1 = dict()
    d2 = dict()
    dtemp = dict()
    

    
    for i in l1:
        dtemp[i] = 0
    
    for i in l1:
        dtemp[i] += 1
    
    print (dtemp)
    
    for i in l1:
        d1[i] = d1.get(i, 0) + 1
    
    for i in l2:
        d2[i] = d2.get(i, 0) + 1
    
    print (d1)
    print (d2)
    
    if d1 == d2:
        return True
    else:
        return False
        
        

l1 = "abbd"
l2 = "bbda"
print(anagram(l1, l2))
 
items = [1,2,2,3,4,4]
items2 = [1,2,3,3]
# print(set(items) - set(items2))       