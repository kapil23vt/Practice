def zillow(s):
    s = s.strip('#')
    
    R = int(s[0:2],16)
    G = int(s[2:2+2], 16)
    B = int(s[4:4+2], 16)
    
    print(R,G,B)
    
    output = B*65536 + G*256 + R 
    
    print(output)
    

s = "#F00"
zillow(s)