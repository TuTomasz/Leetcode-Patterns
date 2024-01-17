
# Problem 1 (1832) Check if the Sentence Is Pangram

# A pangram is a sentence where every letter of the English alphabet appears at least once.
# Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.

# Pseudocode:

# 1. Initialize a set
# 2. Iterate through the string
# 3. Add the current element to the set
# 4. Return len(set) == 26

def checkIfPangram(sentence):
    hash_set = set()
    for c in sentence:
        hash_set.add(c)
    return len(hash_set) == 26
 
 # or 

def checkIfPangram(sentence):
    letters = "abcdefghijklmnopqrstuvwxyz"
        
    hash_set = set(letters)        
    for c in sentence:
        hash_set.discard(c)
        
    if len(hash_set) == 0:
        return True 
    return False


# Problem 2 268. Missing Number (Easy)
# LINK: https://leetcode.com/problems/missing-number/

# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
# Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?

# Pseudocode:

# 1. Initialize a variable sum to 0
# 2. Iterate through the array
# 3. Add the current element to sum
# 4. Return n * (n + 1) / 2 - sum

def missingNumber(nums):
    n = len(nums)
    sum = 0
    for i in range(n):
        sum += nums[i]
    return n * (n + 1) / 2 - sum

# or 

def missingNumber(nums):
    hash_set = set(nums)
    h = len(nums)
        
    for i in range(0,h + 1):
        if i not in hash_set:
            return i 
    return -1 


# Problem 3 1426 Counting Elements (Easy)
# LINK: https://leetcode.com/problems/counting-elements/

# Given an integer array arr, count element x such that x + 1 is also in arr.
# If there're duplicates in arr, count them separately.

# Pseudocode:

# 1. Initialize a variable count to 0
# 2. Initialize a set
# 3. Iterate through the array
# 4. Add the current element to the set
# 5. If the current element + 1 is in the set, then increment count
# 6. Return count

def countElements(arr):
    seen = set(arr)
    count = 0
        
    for i in range(len(arr)):
            
        if arr[i] + 1 in seen:
            count += 1
                
    return count

