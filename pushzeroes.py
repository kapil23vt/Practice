def pushzeros(nums,size):
    
    newarr = []
    for i in range(size):
        if(nums[i] != 0):
            newarr.append(nums[i])
    
    for i in range(len(nums) - len(newarr)):
        newarr.append(0)
    
    print (newarr)

nums = [2,3,0,4,0,0]
size = 6
pushzeros(nums, size)