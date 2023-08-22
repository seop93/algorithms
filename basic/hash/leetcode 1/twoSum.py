
def twoSum(nums, target):

    origin_indices = {}

    for idx, val in enumerate(nums):
        if val in origin_indices:
            origin_indices[val].append(idx)
        else:
            origin_indices[val] = [idx]

    nums.sort()

    l, r = 0, len(nums)-1

    while l < r:
        if target > (nums[l] + nums[r]):
            l += 1
        elif target < (nums[l] + nums[r]):
            r -= 1
        else:
            return [origin_indices[nums[l]][0], origin_indices[nums[r]][-1]]

nums = [6, 7, 10, 23, 10, 7]
target = 14

result = twoSum(nums, target)
print(result)