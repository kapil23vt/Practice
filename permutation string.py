def permute(a, left, right):
    
    if left==right:
        print (''.join(a))
    else:
        for i in range(left,right+1):
            a[left], a[i] = a[i], a[left]
            permute(a, left+1, right)
            a[left], a[i] = a[i], a[left] # backtrack
 
string = "ABC"
n = len(string)
a = list(string)
permute(a, 0, n-1)
