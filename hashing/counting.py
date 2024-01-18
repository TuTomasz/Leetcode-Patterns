
# Problem 1 (Leetcode 340) (Hard)
# LINK: https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/
#Example 1: You are given a string s and an integer k. Find the length of the longest substring that contains at most k distinct characters.

# Pseudocode:

# 1. Initialize left and right pointers to 0
# 2. Initialize a dictionary
# 3. Initialize max_len to 0
# 4. Iterate through the string
# 5. Add the current element to the dictionary
# 6. If the length of the dictionary is greater than k, then subtract the left element from the dictionary and increment left
# 7. Update max_len
# 8. Return max_len

 

def lengthOfLongestSubstringKDistinct(s, k):
    
    left = 0
    right = 0
    max_len = 0
    hash_map = {}
    
    for right in range(len(s)):
        
        hash_map[s[right]] = hash_map.get(s[right], 0) + 1
        
        while len(hash_map) > k:
            hash_map[s[left]] -= 1
            if hash_map[s[left]] == 0:
                del hash_map[s[left]]
            left += 1
        
        max_len = max(max_len, right - left + 1)
    
    return max_len

# or 

def lengthOfLongestSubstringKDistinct(s, k):
 
        from collections import defaultdict

        seen = defaultdict(int)
        ans = 0
        left = 0 
 

        for right in range(len(s)):

            seen[s[right]] += 1

            while len(seen) > k:
                seen[s[left]] -= 1
                if seen[s[left]] == 0:
                    del seen[s[left]] 
                left += 1
            ans = max(ans, right - left + 1)
        
        return ans

# Problem 2 (Leetcode 2248)  Intersection of Multiple Arrays (Medium)

# LINK: https://leetcode.com/problems/intersection-of-multiple-arrays/

# Given an array of arrays, find their intersection. Each element in the result should appear as many times as it shows in every array. The result can be in any order.

# Pseudocode:

# 1. Initialize a dictionary
# 2. Iterate through the array of arrays
# 3. Iterate through the current array
# 4. Add the current element to the dictionary
# 5. If the current element is already in the dictionary, then increment the count
# 6. Initialize an array
# 7. Iterate through the dictionary
# 8. If the count is equal to the length of the array of arrays, then add the element to the result array
# 9. Return the result array

def intersection(nums):
        
        hash_map = {}
        
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                hash_map[nums[i][j]] = hash_map.get(nums[i][j], 0) + 1
        
        result = []
        
        for key, value in hash_map.items():
            if value == len(nums):
                result.append(key)
        
        return result

# or 

def intersection(nums):
            
        from collections import defaultdict
    
        seen = defaultdict(int)
        result = []
            
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                seen[nums[i][j]] += 1
            
        for key, value in seen.items():
            if value == len(nums):
                result.append(key)
            
        return result

# Problem 3 (Leetcode 1941) (Medium) Check if All Characters Have Equal Number of Occurrences

# LINK: https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/

# Given a string s, return true if s is a good string, or false otherwise.
# A string s is good if all the characters that appear in s have the same number of occurrences (i.e., the same frequency).

# Pseudocode:

# 1. Initialize a dictionary
# 2. Iterate through the string
# 3. Add the current element to the dictionary
# 4. If the current element is already in the dictionary, then increment the count
# 5. Initialize a variable count to the value of the first element in the dictionary
# 6. Iterate through the dictionary
# 7. If the value is not equal to count, then return False
# 8. Return True

def areOccurrencesEqual(s):
            
            hash_map = {}
            
            for i in range(len(s)):
                hash_map[s[i]] = hash_map.get(s[i], 0) + 1
            
            count = hash_map[s[0]]
            
            for key, value in hash_map.items():
                if value != count:
                    return False
            
            return True

# or

def areOccurrencesEqual(s):
                    
            from collections import defaultdict
            
            seen = defaultdict(int)
            
            for i in range(len(s)):
                seen[s[i]] += 1
            
            count = seen[s[0]]
            
            for key, value in seen.items():
                if value != count:
                    return False
            
            return True


# problem 4 (Leetcode 560) (Medium) Subarray Sum Equals K

# LINK: https://leetcode.com/problems/subarray-sum-equals-k/

# Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.

# Pseudocode:

# 1. Initialize a dictionary
# 2. Initialize a variable count to 0
# 3. Initialize a variable sum to 0
# 4. Iterate through the array
# 5. Add the current element to sum
# 6. If sum is equal to k, then increment count
# 7. If sum - k is in the dictionary, then increment count by the value of sum - k in the dictionary
# 8. Add sum to the dictionary

def subarraySum(nums, k):
    hash_map = {}
    count = 0
    sum = 0

    for i in range(len(nums)):
        sum += nums[i]

        if sum == k:
            count += 1

        if sum - k in hash_map:
            count += hash_map[sum - k]

        hash_map[sum] = hash_map.get(sum, 0) + 1

    return count

# or

def subarraySum(nums, k):
    from collections import defaultdict
    counts = defaultdict(int)
    counts[0] = 1
    ans = curr = 0

    for num in nums:
        curr += num
        ans += counts[curr - k]
        counts[curr] += 1
    
    return ans


# Problem 5 (Leetcode 1248) (Medium) Count Number of Nice Subarrays

# LINK: https://leetcode.com/problems/count-number-of-nice-subarrays/

# Given an array of integers nums and an integer k. A subarray is called nice if there are k odd numbers on it.
# Return the number of nice sub-arrays.

# Pseudocode:

# 1. Initialize a dictionary
# 2. Initialize a variable count to 0
# 3. Initialize a variable sum to 0
# 4. Iterate through the array
# 5. If the current element is odd, then add 1 to sum
# 6. If sum is equal to k, then increment count
# 7. If sum - k is in the dictionary, then increment count by the value of sum - k in the dictionary

def numberOfSubarrays(nums, k):
    hash_map = {}
    count = 0
    sum = 0

    for i in range(len(nums)):
        if nums[i] % 2 == 1:
            sum += 1

        if sum == k:
            count += 1

        if sum - k in hash_map:
            count += hash_map[sum - k]

        hash_map[sum] = hash_map.get(sum, 0) + 1

    return count

# or

def numberOfSubarrays(nums, k):
    from collections import defaultdict
    counts = defaultdict(int)
    counts[0] = 1
    ans = curr = 0

    for num in nums:
        curr += num % 2
        ans += counts[curr - k]
        counts[curr] += 1
    
    return ans




# Problem 6 (Leetcode 2225) (Medium) Find the Winner of an Array Game

# LINK: https://leetcode.com/problems/find-the-winner-of-an-array-game/

# Given an integer array arr of distinct integers and an integer k.
# A game will be played between the first two elements of the array (i.e. arr[0] and arr[1]).
# In each round of the game, we compare arr[0] with arr[1], the larger integer wins and remains at position 0 and the smaller integer moves to the end of the array.
# The game ends when an integer wins k consecutive rounds.
# Return the integer which will win the game.
# It is guaranteed that there will be a winner of the game.

# Pseudocode:

# initialize dictionary 
# create a map of players and their losses
# iterate through the array
# if the winner is not in the dictionary, add it
# if the looser is not in the dictionary, add it
# else, add the winner to the looser's list of losses
# initialize two arrays
# iterate through the dictionary
# if the length of the list of losses is 0, add the player to the first array
# if the length of the list of losses is 1, add the player to the second array
# sort both arrays
# return the first array

def findWinners(self, matches):
    losses = {}
    for match in matches:
            
        winner = match[0]
        looser = match[1]
            
        if winner not in losses:
            losses[winner] = []
            
            if looser not in losses:
                losses[looser] = [winner]
            else:
                losses[looser].append(winner)
                
        # find palyers with no losses
        
    noLosses = []
    oneLoss = []
        
    for player, results in losses.items():
            
        if len(results) == 0:
            noLosses.append(player)
            
        if len(results) == 1:
            oneLoss.append(player)
                
    noLosses.sort()
    oneLoss.sort()
                
    return [noLosses, oneLoss]

# problem 7 (Leetcode 1133)  (Medium) Largest Unique Number

# LINK: https://leetcode.com/problems/largest-unique-number/

# Given an array of integers A, return the largest integer that only occurs once.
# If no integer occurs once, return -1.

# Pseudocode:

# 1. Initialize a dictionary
# 2. Iterate through the array
# 3. Add the current element to the dictionary
# 4. If the current element is already in the dictionary, then increment the count
# 5. Initialize a variable max to -1


def largestUniqueNumber(nums):
     
    hash_map = {}
    max = -1
    
    for i in range(len(nums)):
        hash_map[nums[i]] = hash_map.get(nums[i], 0) + 1
    
    for key, value in hash_map.items():
        if value == 1:
            max = max(max, key)
    
    return max

# problem 8 (Leetcode 1189)  (Easy) Maximum Number of Balloons

# LINK: https://leetcode.com/problems/maximum-number-of-balloons/

# Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.
# You can use each character in text at most once. Return the maximum number of instances that can be formed.

# Pseudocode:

# 1. Initialize a dictionary
# 2. Iterate through the string
# 3. Add the current element to the dictionary
# 4. If the current element is already in the dictionary, then increment the count
# 5. Initialize a variable min to the value of the first element in the dictionary
# 6. Iterate through the dictionary
# 7. If the key is in the string "balloon", then update min
# 8. Return min

def maxNumberOfBalloons(text):
            
        hash_map = {}
        
        for i in range(len(text)):
            hash_map[text[i]] = hash_map.get(text[i], 0) + 1
        
        min = hash_map["b"]
        
        for key, value in hash_map.items():
            if key in "balloon":
                min = min(min, value)
        
        return min


#############################################
# ADDITIONAL PROBLEMS
#############################################

# 1748. Sum of Unique Elements
# 3005. Count Elements With Maximum Frequency
# 1394. Find Lucky Integer in an Array
# 1207. Unique Number of Occurrences
# 451. Sort Characters By Frequency
# 2958. Length of Longest Subarray With at Most K Frequency
# 1512. Number of Good Pairs
# 930. Binary Subarrays With Sum
# 1695. Maximum Erasure Value
# 567. Permutation in String

# 1. 1748. Sum of Unique Elements
# LINK: https://leetcode.com/problems/sum-of-unique-elements/

# You are given an integer array nums. The unique elements of an array are the elements that appear exactly once in the array.
# Return the sum of all the unique elements of nums.

# Pseudocode:

# 1. Initialize a dictionary
# 2. Iterate through the array
# 3. Add the current element to the dictionary
# 4. If the current element is already in the dictionary, then increment the count
# 5. Initialize a variable sum to 0
# 6. Iterate through the dictionary
# 7. If the value is equal to 1, then add the key to sum
# 8. Return sum

def sumOfUnique(nums):
    from collections import Counter

    counts = Counter(nums)
    sum = 0

    for k,v in counts.items():

        if v <= 1:
            sum += k 

    return sum 


# 2. 3005. Count Elements With Maximum Frequency
# LINK: https://leetcode.com/problems/count-elements-with-maximum-frequency/

# Given an array nums, return the number of elements that are equal to the maximum frequency in the array.

# Pseudocode:

# 1. Initialize a dictionary
# 2. Iterate through the array
# 3. Add the current element to the dictionary
# 4. If the current element is already in the dictionary, then increment the count
# 5. Initialize a variable max to 0
# 6. Iterate through the dictionary

def maxFrequency(nums):
    from collections import Counter

    counts = Counter(nums)
    
    m = max(list(counts.values()))
    
    count = 0 

    for k ,v in counts.items():

        if v == m:
            count += v

    return count 

# 3. 1394. Find Lucky Integer in an Array
# LINK: https://leetcode.com/problems/find-lucky-integer-in-an-array/

# Given an array of integers arr, a lucky integer is an integer which has a frequency in the array equal to its value.
# Return a lucky integer in the array. If there are multiple lucky integers return the largest of them. If there is no lucky integer return -1.

# Pseudocode:

# 1. Initialize a dictionary
# 2. Iterate through the array
# 3. Add the current element to the dictionary
# 4. If the current element is already in the dictionary, then increment the count
# 5. Initialize a variable max to -1
# 6. Iterate through the dictionary
# 7. If the key is equal to the value, then update max
# 8. Return max

def findLucky(arr):
    
    from collections import Counter

    counts = Counter(arr)

    ans = -1 

    for k , v in counts.items():

        if k == v:

            ans = max(ans, v)

    return ans

# 4. 1207. Unique Number of Occurrences
# LINK: https://leetcode.com/problems/unique-number-of-occurrences/

# Given an array of integers arr, write a function that returns true if and only if the number of occurrences of each value in the array is unique.

# Pseudocode:

# 1. Initialize a dictionary
# 2. Iterate through the array
# 3. Add the current element to the dictionary
# 4. If the current element is already in the dictionary, then increment the count
# 5. Initialize a set
# 6. Iterate through the dictionary
# 7. Add the value to the set
# 8. Return the length of the set is equal to the length of the dictionary

def uniqueOccurrences(arr):
     
    from collections import Counter

    counts = Counter(arr)

    uniqueValues =  set(counts.values())
    uniqueKeys = counts.keys()

    if len(uniqueValues) == len(uniqueKeys):
        return True
    return False




