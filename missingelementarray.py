def missingelement(arr,size):
    d =dict()
    
    for i in arr:
        d[i] = i
        
    print (d)
    
    for i in range(size):
        if i not in d:
            print (i)


arr = [0,1,2,3,5]
size = 6
missingelement(arr, size)