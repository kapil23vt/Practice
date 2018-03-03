def nextClosestTime(time):
    digits = [int(y) for x in time.split(':') for y in x]
    
    print (digits)
    
    h, m = time.split(':')
    
    print(h,m)
    
    while True:
        
        if int(m) == 59:
            h,m = (str(int(h)+1), '00')
        else:
            h,m = h, str(int(m)+1)
        #h, m =  if int(m) == 59 else ()

        
        if len(h) == 1:
            h = '0' + h
        else:
            h = h
        
        #h = '00' if int(h) > 23 else h
        #h = '0' + h if len(h) == 1 else h
        
        if (len(m) == 1):
            m = '0'+ m
        else:
            m = m
        
        #m = '0' + m if len(m) == 1 else m
        
        if all([int(x) in digits for x in h+m]):
            return h + ':' + m


print(nextClosestTime('11:00'))
