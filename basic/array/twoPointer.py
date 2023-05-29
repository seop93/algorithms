def twoSum(nums, target):
    nums.sort()
    l, r = 0, len(nums) - 1
    while l < r:
        if nums[l] + nums[r] == target:
            return True
        elif nums[l] + nums[r] <= target:
            l += 1
        else:
            r -= 1

    return False

print(twoSum([1,23,4,6,7,23,], 7))       