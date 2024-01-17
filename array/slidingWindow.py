###############################################
# Sliding Window Problems
###############################################


# Problem 1:   NOT LEETCODE
# LINK:   
# Given an array of positive integers nums and an integer k, find the length of the longest subarray
# whose sum is less than or equal to k.

# Pseudocode:

# 1. Initialize left and right pointers to 0
# 2. Initialize max_len and curr_sum to 0
# 3. Iterate through the array
# 4. Add the current element to curr_sum
# 5. If curr_sum > k, then subtract the left element from curr_sum and increment left
# 6. Update max_len
# 7. Return max_len


def longestSubarray(nums, k):
    left = 0
    right = 0
    max_len = 0
    curr_sum = 0

    for right in range(len(nums)):
        curr_sum += nums[right]

        while curr_sum > k:
            curr_sum -= nums[left]
            left += 1

        max_len = max(max_len, right - left + 1)

    return max_len


# Problem 2:

# You are given a binary substring s (a string containing only "0" and "1").
# An operation involves flipping a "0" into a "1". What is the length of the longest substring
# containing only "1" after performing at most one operation?For example, given s = "1101100111",
# the answer is 5. If you perform the operation at index 2, the string becomes 1111100111.

# Pseudocode:

# 1. Initialize left and right pointers to 0
# 2. Initialize max_len and curr_sum to 0
# 3. Iterate through the array
# 4. If the current element is 0, then increment curr_sum
# 5. If curr_sum > 1, then subtract the left element from curr_sum and increment left
# 6. Update max_len
# 7. Return max_len


def longestSubstring(s):
    left = 0
    right = 0
    max_len = 0
    curr_sum = 0

    for right in range(len(s)):

        if s[right] == 0:
            curr_sum += 1

        while curr_sum > 1:
            if s[left] == 0:
                curr_sum -= 1
            left += 1

        max_len = max(max_len, right - left + 1)

    return max_len


# Problem 3: (Leetcode 1004) (Medium)
# LINK: https://leetcode.com/problems/max-consecutive-ones-iii/

# Given a binary array nums and an integer k, return the maximum number of consecutive 1's
# in the array if you can flip at most k 0's.

# Pseudocode:

# 1. Initialize left and right pointers to 0
# 2. Initialize max_len and curr_sum to 0
# 3. Iterate through the array
# 4. If the current element is 0, then increment curr_sum
# 5. If curr_sum > k, then subtract the left element from curr_sum and increment left
# 6. Update max_len
# 7. Return max_len


def longestOnes(nums, k):
    left = 0
    right = 0
    max_len = 0
    curr_sum = 0

    for right in range(len(nums)):

        if nums[right] == 0:
            curr_sum += 1

        while curr_sum > k:  # only difference from previous problem
            curr_sum -= nums[left]
            left += 1

        max_len = max(max_len, right - left + 1)

    return max_len


# Problem 4: (Leetcode 713) (Medium)
# LINK: https://leetcode.com/problems/subarray-product-less-than-k/

# Given an array of integers nums and an integer k, return the number of contiguous subarrays
# where the product of all the elements in the subarray is strictly less than k.

# Pseudocode:

# 1. Initialize left and right pointers to 0
# 2. Initialize number and curr_prod to 1
# 3. Iterate through the array
# 4. Multiply the current element to curr_prod
# 5. If curr_prod >= k, then divide the left element from curr_prod and increment left
# 6. Update number
# 7. Return number


def numSubarrayProductLessThanK(nums, k):
    left = 0
    right = 0
    number = 0
    curr_prod = 1

    for right in range(len(nums)):
        curr_prod *= nums[right]

        while curr_prod >= k:
            curr_prod //= nums[left]
            left += 1

        number += right - left + 1

    return number


# Problem 5: (Leetcode 209) (Medium)
# LINK: https://leetcode.com/problems/minimum-size-subarray-sum/

# Given an array of positive integers nums and a positive integer target, return the minimal length of
# a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

# Pseudocode:

# 1. Initialize left and right pointers to 0
# 2. Initialize ans and curr to 0
# 3. Iterate through the array
# 4. Add the current element to curr
# 5. While curr >= target, update ans and subtract the left element from curr and increment left
# 6. Return ans


def minSubArrayLen(s, nums):
    target = s
    curr = 0
    left = 0
    ans = float("inf")

    for right in range(len(nums)):

        curr += nums[right]

        while curr >= target:
            ans = min(ans, right - left + 1)
            curr -= nums[left]
            left += 1

    if ans == float("inf"):
        return 0
    return ans


# Problem 6: (Leetcode 1456) (Medium)
# LINK: https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/

# Given a string s and an integer k, return the maximum number of vowel letters in any substring
# of s with length k. Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

# Pseudocode:

# 1. Initialize left and right pointers to 0
# 2. Initialize ans and curr to 0
# 3. Iterate through the array and check if the current element is a vowel
# 4. If it is, then increment curr
# 5. If right - left + 1 > k, then check if the left element is a vowel
# 6. If it is, then decrement curr and increment left
# 7. Update ans
# 8. Return ans


def maxVowels(s, k):
    vowels = set(["a", "e", "i", "o", "u"])

    left = 0
    ans = 0
    curr = 0

    for right in range(len(s)):
        if s[right] in vowels:
            curr += 1
        if right - left + 1 > k:
            if s[left] in vowels:
                curr -= 1
                left += 1
            else:
                left += 1
        if right - left + 1 == k:
            ans = max(ans, curr)
    return ans

# Problem 7: (Leetcode 1208)  (Medium)
# LINK: https://leetcode.com/problems/get-equal-substrings-within-budget/

# You are given two strings s and t of the same length. You want to change s to t. Changing the i-th character of s to
# i-th character of t costs |s[i] - t[i]| that is, the absolute difference between the ASCII values of the characters.
# You are also given an integer maxCost.
# Return the maximum length of a substring of s that can be changed to be the same as the corresponding substring of t
# with a cost less than or equal to maxCost.
# If there is no substring from s that can be changed to its corresponding substring from t, return 0.

# Pseudocode:

# 1. Initialize left and right pointers to 0
# 2. Initialize ans and curr to 0
# 3. Iterate through the array
# 4. Add the absolute difference of the current elements to curr
# 5. If curr > maxCost, then subtract the absolute difference of the left element from curr and increment left
# 6. Update ans
# 7. Return ans

def equalSubstring(s, t, maxCost):
    left = 0
    ans = 0
    curr = 0

    for right in range(len(s)):
        curr += abs(ord(s[right]) - ord(t[right]))

        while curr > maxCost:
            curr -= abs(ord(s[left]) - ord(t[left]))
            left += 1

        ans = max(ans, right - left + 1)

    return ans


# Problem 8: (Leetcode 2379) (Easy)
# LINK: https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/
#  Minimum Recolors to Get K Consecutive Black Blocks
# You are given a 0-indexed string blocks of length n, where blocks[i] is either 'W' or 'B', representing the color of the ith block. The characters 'W' and 'B' denote the colors white and black, respectively.
# You are also given an integer k, which is the desired number of consecutive black blocks.
# In one operation, you can recolor a white block such that it becomes a black block.
# Return the minimum number of operations needed such that there is at least one occurrence of k consecutive black blocks.

# Pseudocode:

# 1. Initialize left and right pointers to 0
# 2. Initialize ans and curr to 0
# 3. Iterate through the array
# 4. If the current element is W, then increment curr
# 5. If curr > k, then check if the left element is W
# 6. If it is, then decrement curr and increment left
# 7. Update ans
# 8. Return ans

def minRecolors(blocks, k):
    left = 0 
    right = 0 
    curr = 0 
    ans = float('inf')

    for right in range(len(blocks)):

        if blocks[right] == "W":
            curr += 1 
           
        if right - left + 1  >= k: 
            ans = min(ans, curr)
            if blocks[left] == "W":
                curr -= 1
            left += 1

    if ans == float('inf'):
        return 0 
    return ans


# Problem 9: (Leetcode 485) (easy)

# LINK: https://leetcode.com/problems/max-consecutive-ones/

# Given a binary array nums, return the maximum number of consecutive 1's in the array.

# Pseudocode:

# 1. Initialize left and right pointers to 0
# 2. Initialize ans and curr to 0
# 3. Iterate through the array
# 4. If the current element is 1, then increment curr
# 5. while curr > 0, then check if the left element is 1
# 6. If it is, then decrement curr and increment left
# 7. Update ans

def findMaxConsecutiveOnes(nums):
    curr = 0  
    left = 0 
    ans = 0 

    for right in range(len(nums)):

        if nums[right] == 0:
            curr += 1

        while curr > 0:

            if nums[left] == 0:
                curr -= 1
            left += 1
            
        ans = max(ans, right - left + 1)
        
    return ans

# problem 10 (Leetcode 209) (Medium)
# LINK: https://leetcode.com/problems/minimum-size-subarray-sum/

# Given an array of positive integers nums and a positive integer target, return the minimal length of
# a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

# Pseudocode:

# 1. Initialize left and right pointers to 0
# 2. Initialize ans and curr to 0
# 3. Iterate through the array
# 4. Add the current element to curr
# 5. While curr >= target, update ans and subtract the left element from curr and increment left
# 6. Return ans

def minSubArrayLen(s, nums):
    target = s
    curr = 0
    left = 0 
    ans = float('inf')

    for right in range(len(nums)):

        curr += nums[right]

        while curr >= target:
            
            ans = min( ans, right-left + 1)
            curr -= nums[left]
            left += 1


    if ans == float('inf'): 
        return 0
    return ans

# problem 11 (Leetcode 1456) (Medium)
# LINK: https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/

# Given a string s and an integer k, return the maximum number of vowel letters in any substring
# of s with length k. Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

# Pseudocode:

# 1. Initialize left and right pointers to 0
# 2. Initialize ans and curr to 0
# 3. Iterate through the array and check if the current element is a vowel
# 4. If it is, then increment curr
# 5. If right - left + 1 > k, then check if the left element is a vowel
# 6. If it is, then decrement curr and increment left
# 7. Update ans
# 8. Return ans

def maxVowels(s, k):
    vowels = set(['a', 'e', 'i', 'o', 'u'])
    left = 0 
    ans = 0 
    curr = 0

    for right in range(len(s)):

        if s[right] in vowels:
            curr += 1
        
        if right - left + 1 > k: 

            if s[left] in vowels:
                curr -= 1 
            left += 1
            
        if right - left + 1 == k :
            ans = max(ans, curr)
            
    return ans
    


###############################################
# sliding window problems static window size
###############################################

# Problem 1: find max average (Easy)
# LINK: https://leetcode.com/problems/maximum-average-subarray-i/

# Given an array consisting of n integers, find the contiguous subarray of given length k that has the maximum average
# value. And you need to output the maximum average value.

# Pseudocode:

# 1. Initialize curr and avg to 0
# 2. Iterate through the array
# 3. Add the current element to curr
# 4. If i >= k, then subtract the element at i - k from curr
# 5. Update avg
# 6. Return avg

def findMaxAverage(nums, k):
    avg = 0
    curr = 0

    for i in range(k):
        curr += nums[i]
    
    avg = curr / k

    for i in range(k, len(nums)):
        curr += nums[i] - nums[i - k]
        avg = max(avg, curr / k)
    
    return avg



# Problem 2: 1456. Maximum Number of Vowels in a Substring of Given Length (Medium)

# LINK: https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/

# Given a string s and an integer k.
# Return the maximum number of vowel letters in any substring of s with length k.
# Vowel letters in English are (a, e, i, o, u).

# Pseudocode:

# 1. Initialize left and right pointers to 0
# 2. Initialize ans and curr to 0
# 3. Iterate through the array and check if the current element is a vowel
# 4. If it is, then increment curr
# 5. If right - left + 1 > k, then check if the left element is a vowel
# 6. If it is, then decrement curr and increment left
# 7. Update ans
# 8. Return ans

def maxVowels(s, k):
    vowels = set(["a", "e", "i", "o", "u"])

    left = 0
    ans = 0
    curr = 0

    for right in range(len(s)):
        if s[right] in vowels:
            curr += 1
        if right - left + 1 > k:
            if s[left] in vowels:
                curr -= 1
                left += 1
            else:
                left += 1
        if right - left + 1 == k:
            ans = max(ans, curr)
    return ans

