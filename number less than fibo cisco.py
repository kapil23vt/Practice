def functionn(n):
    
    first = 0
    second = 1
    next = first + second
    
    while next < n:
        
        first = second
        second = next
        next = first + second
    
    return (second)
        
print (functionn(15))