import numpy as np
def conv(a,b):
    lena = len(a)
    lenb = len(b)
    
    lenans = len(a) - len(b) + 1
    ans = []
    
    for i in range(lenans):
        ans.append(0)
    
    #for i in np.arange(lena):
        #for j in np.arange(lenb):
            
            #ans[i+j] += a[i] * b[j]
            
    lengthA=np.size(a)
    lengthB=np.size(b)
    
    C = np.zeros(lengthA + lengthB -1)
    
    for m in np.arange(lengthA):
        for n in np.arange(lengthB):
            C[m+n] = C[m+n] + a[m]*b[n]
    print (C) 
         
    
a = [2,3,4,5]
b = [1,2]

conv(a,b)