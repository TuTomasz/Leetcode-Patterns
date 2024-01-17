
# Problem  1 2270. Number of Ways to Split Array

# Given an integer array nums, return the number of ways to split the array into three non-empty subarrays with the
# sum of the elements in each subarray equal.

 
def waysToSplit(nums):
    n = len(nums)
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + nums[i]
    ans = 0

    for i in range(n - 1):
        left_section = prefix[i]
        right_section = prefix[n] - prefix[i]
        if left_section > right_section:
            ans += 1
    return ans



# Problem 2: Running Sum of 1d Array (Easy)
# LINK: https://leetcode.com/problems/running-sum-of-1d-array/

# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
#
# Return the running sum of nums.

# Pseudocode:

# 1. Initialize a variable sum to 0
# 2. Iterate through the array
# 3. Add the current element to sum
# 4. Update the current element to sum
# 5. Return nums

def runningSum(nums):
    sum = 0
    for i in range(len(nums)):
        sum += nums[i]
        nums[i] = sum
    return nums


# Problem 3: Minimum Value to get Positive Step by Step Sum (Easy)
# LINK: https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum/

# Given an array of integers nums, you start with an initial positive value startValue.
#
# In each iteration, you calculate the step by step sum of startValue plus elements in nums (from left to right).
#
# Return the minimum positive value of startValue such that the step by step sum is never less than 1.

# Pseudocode:

# 1. Initialize a variable sum to 0
# 2. Initialize a variable min to 0
# 3. Iterate through the array
# 4. Add the current element to sum
# 5. Update min to min(min, sum)
# 6. Return 1 - min


def minStartValue(nums):

    prefix = [nums[0]] * len(nums)

    for i in range(1, len(nums)):

        prefix[i] = prefix[i - 1 ] + nums[i]

    minPrefix = min(prefix)


    minPrefix = min(prefix)
        
    if minPrefix < 0:
        return abs(minPrefix) + 1
    return 1


# Problem 4: K Radius Subarray Averages (Easy)
# LINK: https://leetcode.com/problems/average-of-levels-in-binary-tree/

# You are given a 0-indexed array nums of n integers, and an integer k.

# The k-radius average for a subarray of nums centered at some index i with the radius k is the average of all elements in nums between the indices i - k and i + k (inclusive). If there are less than k elements before or after the index i, then the k-radius average is -1.

# Build and return an array avgs of length n where avgs[i] is the k-radius average for the subarray centered at index i.

# The average of x elements is the sum of the x elements divided by x, using integer division. The integer division truncates toward zero, which means losing its fractional part.

# Pseudocode:

# 1. Initialize a variable sum to 0
# 2. Initialize a variable avg to 0
# 3. Initialize a variable left to 0
# 4. Iterate through the array
# 5. Add the current element to sum
# 6. If i >= k, then subtract the element at i - k from sum
# 7. If i >= k - 1, then update avg to sum / k
# 8. Return avg

def kRadiusSubarrayAverages(nums, k):
        n = len(nums)
        result = [-1 for i in range(n)]
        if k == 0:
            return nums
        leftSum = [0 for i in range(n)]
        leftSum[0] = nums[0]
        for i in range(1,len(nums)):
            leftSum[i] = (leftSum[i-1]+nums[i])
        for i in range(k,n-k):
            if i == k:
                result[i] = leftSum[i+k]//(2*k+1)
            else:
                result[i] = (leftSum[i+k]-leftSum[i-k-1])//(2*k+1)
        return result

# Problem 5: (1732) Find the Highest Altitude

# There is a biker going on a road trip. The road trip consists of n + 1 points at different altitudes. The biker starts
# his trip on point 0 with altitude equal 0.
#
# You are given an integer array gain of length n where gain[i] is the net gain in altitude between points i​​​​​​ and
# i + 1 for all (0 <= i < n). Return the highest altitude of a point.

# Pseudocode:

# 1. Initialize a variable max to 0
# 2. Initialize a variable curr to 0
# 3. Iterate through the array
# 4. Add the current element to curr
# 5. Update max to max(max, curr)
# 6. Return max

def largestAltitude(gain):
    max = 0
    curr = 0

    for i in range(len(gain)):
        curr += gain[i]
        max = max(max, curr)
    return max

def largestAltitude(gain):
    prefix = [0] * (len(gain) + 1 )
    prefix[1] = gain[0]

    for i in range(2,len(prefix)):

        prefix[i] = prefix[i -1] + gain[i - 1]

    return max(prefix)


# Problem 6: (724) Find Pivot Index

# Given an array of integers nums, calculate the pivot index of this array.
#
# The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum
# of all the numbers strictly to the index's right.
#
# If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left.
# This also applies to the right edge of the array.
#
# Return the leftmost pivot index. If no such index exists, return -1.

# Pseudocode:

# 1. Initialize a variable sum to 0
# 2. Iterate through the array
# 3. Add the current element to sum
# 4. Initialize a variable left to 0
# 5. Iterate through the array
# 6. If left == sum - left - nums[i], then return i
# 7. Add the current element to left
# 8. Return -1

def pivotIndex(nums):
    sum = 0
    for i in range(len(nums)):
        sum += nums[i]

    left = 0
    for i in range(len(nums)):
        if left == sum - left - nums[i]:
            return i
        left += nums[i]
    return -1


# Problem 7: (303) Range Sum Query - Immutable

# Given an integer array nums, handle multiple queries of the following type:
#
# Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
# Implement the NumArray class:
#
# NumArray(int[] nums) Initializes the object with the integer array nums.
# int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive
# (i.e. nums[left] + nums[left + 1] + ... + nums[right]).
#
# Pseudocode:

# 1. Initialize a variable sum to 0
# 2. Iterate through the array
# 3. Add the current element to sum
# 4. Initialize a variable left to 0
# 5. Iterate through the array
# 6. If left == sum - left - nums[i], then return i
# 7. Add the current element to left
# 8. Return -1

class NumArray:
    
        def __init__(self, nums):
            self.prefix = []
            self.curr = 0
            for i in range(len(nums)):
                self.curr += nums[i]
                self.prefix.append(self.curr)
    
        def sumRange(self, left, right):
            if left == 0:
                return self.prefix[right]
            return self.prefix[right] - self.prefix[left - 1]

