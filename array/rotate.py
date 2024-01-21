# 189. Rotate Array

# Given an array, rotate the array to the right by k steps, where k is non-negative.

# Pseudocode:

# 1. Reverse the entire array
# 2. Reverse the first k elements
# 3. Reverse the remaining elements
# 4. Return the array

def rotate(nums, k):
    k %= len(nums)
    reverse(nums, 0, len(nums) - 1)
    reverse(nums, 0, k - 1)
    reverse(nums, k, len(nums) - 1)
    return nums

def reverse(nums, start, end):
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start, end = start + 1, end - 1