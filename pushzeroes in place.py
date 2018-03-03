def pushzerosinplace(nums,size):
    
    count = 0
    helper = 0
    
    for i in range(size):
        if nums[i] == 0:
            count += 1
        if nums[i] != 0:
            nums[helper] = nums[i]
            helper += 1
    
    for i in range(count):
        nums[helper] = 0
        helper += 1
    
    print (nums) 
    
nums = [2,3,0,4,0,0, 1]
size = len(nums)
pushzerosinplace(nums, size)