# 0 1 2 1 0
# low = 0 , high = 5, mid = 2
# start compare from mid upto high
# as per conditions, we fill low, mid and high positions
# if mid element = 0, move it start of array (low++, mid++)
# if mid element = 1, it is at correct location(mid++)
# if mid element = 2, move to end of array(high--)

def sort012(a, arr_size):
    lo = 0
    hi = arr_size - 1
    index = 0
    while index <= hi:
        if a[index] > 0:
            a[lo],a[index] = a[index],a[lo]
            lo = lo + 1
            index = index + 1
        elif a[index] < 0:
            index = index + 1
        else:
            a[index],a[hi] = a[hi],a[index] 
            hi = hi - 1
    return a
     
def printArray( a):
    for k in a:
        print (k)
     
arr = [5,-3,-2,4,0,2,1]
arr_size = len(arr)
arr = sort012( arr, arr_size)
printArray(arr)



