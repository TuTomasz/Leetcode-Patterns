# Greedy problems are not an algorythm but a way of thinking.
# Most greedy problems will be asking for the maximum or minimum of something, but not always.

# 2126 Destroy Asteroids 
# https://leetcode.com/problems/destroying-asteroids/

# Pseudocode:

# 1. sort the array 
# 2. iterate through the array
# 3. if the current element is bigger then mass of the current planet 
# 4. then add the current element to the result 
# 5. else return false if asteroid is bigger then planet

# O(n⋅logn) time | O(1) space
def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:

    asteroids.sort()
    planet = mass

    for asteroid in asteroids:
        if asteroid > planet:
            return False

        planet += asteroid
    
    return True


# 2294. Partition Array Such That Maximum Difference Is K

# Description

# You are given an integer array nums and an integer k. You may partition nums into one or more subsequences such that each element in nums appears in exactly one of the subsequences.
# Return the minimum number of subsequences needed such that the difference between the maximum and minimum values in each subsequence is at most k.
# A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.


# https://leetcode.com/problems/partition-array-such-that-maximum-sum-is-k/

# Pseudocode:

# sort the array
# initialie ans to 1  because we have at least one partition
# set curr to the first element of the array
# iterate through the array from 1 to the end
# if the current element minus curr is bigger then k
# then update curr to the current element
# and update ans to ans + 1
# return ans

#  O(n⋅logn) time | O(1) space

def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
    arr.sort()
    ans = 1
    curr = arr[0]

    for i in range(1, len(arr)):
        if arr[i] - curr > k:
            curr = arr[i]
            ans += 1
    
    return ans
    



# 1481. Least Number of Unique Integers after K Removals

# https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals/

# Description 

# Given an array of integers arr and an integer k. Find the least number of unique integers after removing exactly k elements.

# Pseudocode:

# 1. Count the frequency of each number
# 2. Sort the frequency array in descending order by frequency
# 3. While k:
# 4.     If the last element of the frequency array is less than or equal to k:
# 5.         Update k to k - last element of the frequency array
# 6.         Pop the last element of the frequency array
# 7.     Else:
# 8.         Break
# 9. Return the length of the frequency array


# O(n⋅logn) time | O(n) space

def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
    from collections import Counter

    counts = Counter(arr)

    freq = sorted(counts.values(),reverse=True)

    while k:
        val = freq[-1]
        if val <= k:
            k -= val
            freq.pop()
        else:
            break

    return len(freq)