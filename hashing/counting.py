

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

        if sum == k:    ## dont need this line if you initalize hahmap with {0:1}
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

# 5. 451. Sort Characters By Frequency
# LINK: https://leetcode.com/problems/sort-characters-by-frequency/

# Given a string s, sort it in decreasing order based on the frequency of characters, and return the sorted string.

# Pseudocode:

# 1. Initialize a dictionary
# 2. Iterate through the string
# 3. Add the current element to the dictionary
# 4. If the current element is already in the dictionary, then increment the count
# 5. Initialize an array
# 6. Iterate through the dictionary
# 7. Append the key to the array count times
# 8. Sort the array in reverse order
# 9. Return the array as a string

def frequencySort(s):
    
    from collections import Counter

    counts = Counter(s)

    freq = []
    for k , v in counts.items():
        freq.append([k,v])
    freq.sort(key=lambda x:x[1], reverse=True)

    res = ""
    for el in freq:
        res += el[0] * el[1]
    return res





# 7. 1512. Number of Good Pairs
# LINK: https://leetcode.com/problems/number-of-good-pairs/

# Given an array of integers nums.
# A pair (i,j) is called good if nums[i] == nums[j] and i < j.
# Return the number of good pairs.

# Pseudocode:

# 1. Initialize a dictionary
# 2. Initialize a variable count to 0
# 3. Iterate through the array
# 4. Add the current element to the dictionary
# 5. If the current element is already in the dictionary, then increment count by the value of the current element in the dictionary
# 6. Return count

def numIdenticalPairs(nums):
    dic = {}
       
    res = 0
    for n in nums:
        
        if n not in dic:
            dic[n] = 1
        else:
            res += dic[n]
            dic[n] +=1
    
    return res


# 10. 567. Permutation in String
# LINK: https://leetcode.com/problems/permutation-in-string/

# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
# In other words, return true if one of s1's permutations is the substring of s2.

# Pseudocode:

# 1. Initialize a dictionary
# 2. Iterate through the string s1
# 3. Add the current element to the dictionary
# 4. If the current element is already in the dictionary, then increment the count
# 5. Initialize a variable left to 0
# 6. Initialize a variable right to 0
# 7. Initialize a variable count to 0
# 8. Iterate through the string s2
# 9. If the current element is in the dictionary, then decrement the count
# 10. If the count is equal to 0, then increment right
# 11. If the count is less than 0, then increment left and update the count
# 12. If right - left is equal to the length of s1, then return True
# 13. Return False

def checkInclusion(s1, s2):
    
    from collections import Counter

    counts = Counter(s1)
    left = 0 
    right = 0 
    count = len(s1)

    while right < len(s2):

        if s2[right] in counts:
            count -= 1

        if count == 0:
            return True

        if right - left + 1 == len(s1):
            if s2[left] in counts:
                count += 1
            left += 1

        right += 1

    return False

# or

def checkInclusion(s1, s2):
    from collections import Counter

    seen = Counter(s1)
    left = 0
    right = 0 

    while right < len(s2):
        if s2[right] in seen:
            if seen[s2[right]] == 1:
                del seen[s2[right]]
                if len(seen) == 0:
                    return True
            else:
                seen[s2[right]] -= 1
            right += 1
        else:
            seen[s2[left]] += 1
            left += 1
        
    if len(seen) == 0:
        return True
    return False


# 11. 219. Contains Duplicate II

# LINK: https://leetcode.com/problems/contains-duplicate-ii/

# Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j]
# and abs(i - j) <= k.

# Pseudocode:

# 1. Initialize a dictionary
# 2. Iterate through the array
# 3. If the current element is in the dictionary and the difference between the current index and the value of the current element in the dictionary
#    is less than or equal to k, then return True
# 4. Add the current element to the dictionary

def containsNearbyDuplicate(nums, k):
    seen = {}

    for i , el in enumerate(nums):
        if el in seen and i - seen[el]  <= k: # seen[el] is j 
            return True 
        seen[el] = i 
    return False 
