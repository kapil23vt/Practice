def modify(s):
    R = int(s[1:3],16)
    G = int(s[3:5],16)
    B = int(s[5:7],16)
    
    return R,G,B

def zillow(temp):
    
    if (temp[0]!= '#'):
        print ("Incorrect input")
        exit()
    
    x = len(temp)
    newstring = '#'
    
    if (x > 4):
        R,G,B = modify(temp)
        print (R,G,B)
    # else:
        # s = temp
    
    if ( x<= 4):
        for i in range(1,len(temp)):
            newstring += temp[i]
            newstring += temp[i]
        
        print (newstring)
        R,G,B = modify(newstring)
            
        
        
    
    print(temp)
    print(R,G,B)
    
    
    output = B*65536 + G*256 + R 
    print (output)
    

s = "#800080"
zillow(s)

