# 53. Maximum Subarray

# LINK: https://leetcode.com/problems/maximum-subarray/
#
# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

# Pseudocode:

# 1. Initialize a variable max_sum to -inf
# 2. Initialize a variable sum to 0
# 3. Iterate through the array
# 4. Add the current element to sum
# 5. Update max_sum to max(max_sum, sum)
# 6. If sum is less than 0, then update sum to 0
# 7. Return max_sum

def maxSubArray(nums):
    localMax = nums[0]
    globalMax = nums[0]
    
    for i in range(1,len(nums)):
        
        localMax = max( nums[i] + localMax , nums[i])
        globalMax = max(localMax,globalMax)

    return globalMax