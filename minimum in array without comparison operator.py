 
def minimum(x,y):
    c = 0
    while (x>0 and y>0): 
     
        x=x-1
        y=y-1
        c=c+1
     
    return c
  
def arrayMinimum(A,N):
 
    mn = A[0]
  
    #for i in range(N-1,0,-1):
    for i in range(N):  
        mn = minimum(mn, A[i])    
  
    return mn
     
A = [ 2, 3, 1, 4, 10]
N =len(A)
 
print(arrayMinimum(A, N))