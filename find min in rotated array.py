def findMin(nums):
    low = 0
    high = len(nums) - 1
    
    while low < high:
        mid = int((low+high)/2)
        
        if (nums[mid] > nums[high]):
            low = mid + 1
        else:
            high = mid
    
    return nums[low]

nums = [2,3,3,0,0,1,1,2]
# low = 0, high = 6, mid = 3
# comparing 7 with last element 
# since it is greater than last element
# you know lowest number is after current mid
# so make low = mid + 1
# if not then move high to mod
print(findMin(nums))