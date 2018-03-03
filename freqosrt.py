# from adodbapi.adodbapi import counter

def fsort(s):
    import collections
    if not s:
        return ""
    count = collections.Counter(s)
    counter = count.most_common()
    
    print (count)
    print (counter)
    
    result = ""
    
    for i in counter:
        result = result + i[0]*i[1]
        # print (i)
        # print (j)
    
    print (result)    
    
    
s1 = "abbccc"
print(fsort(s1))

from collections import Counter
c = Counter([1,2,5,3,4,1,2,3])

print (list(c.elements()))
print (c.most_common(5))        