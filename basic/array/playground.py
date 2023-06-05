def twoSum(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i+1, n):
            if nums[i] + nums[j] == target:
                return True
            
    return False

print(twoSum([1,23,3,5,325,324,3], target=23))

