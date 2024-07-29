def twoSum(nums, target):
    num_to_index = {}

    for index, num in enumerate(nums):
        complement = target - num

        if complement in num_to_index:
            return [num_to_index[complement], index]

        num_to_index[num] = index

print(twoSum([2, 7, 11, 15], 9))      # Output: [0, 1]
print(twoSum([3, 2, 4], 6))           # Output: [1, 2]
print(twoSum([3, 3], 6))              # Output: [0, 1]
print(twoSum([-1, -2, -3, -4, -5], -8)) # Output: [2, 4]
print(twoSum([0, 4, 3, 0], 0))        # Output: [0, 3]
