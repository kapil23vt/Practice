def twosum(nums, target):
    
    d = dict()
    
    for i in range(len(nums)):
        d[nums[i]] = i;
    
    print (d)
    
    for i in range(len(nums)):
        key = target - nums[i]
        
        if key in d:
            print (i)
            print (d[key])
    
    
    


nums = [4,5,6,7,8]
target = 9
twosum(nums, target)