# 128. Longest Consecutive Sequence
# link : https://leetcode.com/problems/longest-consecutive-sequence/

# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# Pseudocode:

# 1. Initialize a set
# 2. Add all the elements of the array to the set
# 3. Initialize a variable max_len to 0
# 4. Iterate through the array
# 5. If the current element - 1 is not in the set, then
# 6. Initialize a variable curr_len to 1
# 7. Initialize a variable curr_num to the current element
# 8. While curr_num + 1 is in the set, then
# 9. Increment curr_len
# 10. Increment curr_num
# 11. Update max_len to max(max_len, curr_len)

#            4   x
#            3 x 4
#  x   x  x  2 4 3
# [100,4,200,1,3,2]   
#            ^
#            |
def longestConsecutive(nums):
    nums = set(nums)
    max_len = 0

    for num in nums:
        if num - 1 not in nums:  # start of a sequence pervent duplicate counting
            curr_len = 1
            curr_num = num

            while curr_num + 1 in nums:
                curr_len += 1
                curr_num += 1

            max_len = max(max_len, curr_len)

    return max_len