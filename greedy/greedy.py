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


#  881 Boats to Save People

# https://leetcode.com/problems/boats-to-save-people/

# Description

# The i-th person has weight people[i], and each boat can carry a maximum weight of limit.
# Each boat carries at most 2 people at the same time, provided the sum of the weight of those people is at most limit.
# Return the minimum number of boats to carry every given person.  (It is guaranteed each person can be carried by a boat.)

# Pseudocode:

# 1. Sort the array
# 2. Initialize a variable ans to 0
# 3. Initialize a variable left to 0
# 4. Initialize a variable right to n - 1
# 5. While left <= right:
# 6.     If people[left] + people[right] <= limit:
# 7.         Increment left
# 10.    Decrement right
# 11.    Increment ans
# 12. Return ans

# O(n⋅logn) time | O(1) space

def numRescueBoats(self, people: List[int], limit: int) -> int:
    
    lightest = 0 
    heaviest = len(people) - 1

    ans = 0
    people.sort()

    while lightest <= heaviest: 

        if people[lightest] + people[heaviest] <= limit:
            lightest += 1

        heaviest -= 1
        ans += 1

    return ans

# 1710. Maximum Units on a Truck

# https://leetcode.com/problems/maximum-units-on-a-truck/

# Description

# You are assigned to put some amount of boxes onto one truck. You are given a 2D array boxTypes, where boxTypes[i] = [numberOfBoxesi, numberOfUnitsPerBoxi]:

# numberOfBoxesi is the number of boxes of type i.
# numberOfUnitsPerBoxi is the number of units in each box of the type i.
# You are also given an integer truckSize, which is the maximum number of boxes that can be put on the truck. You can choose any boxes to put on the truck as long as the number of boxes does not exceed truckSize.
# Return the maximum total number of units that can be put on the truck.

# Pseudocode:

# 1. Sort the array by the number of units per box in descending order
# 2. Initialize a variable ans to 0
# 3. Initialize a variable i to 0
# 4. While truckSize and i < n:
# 5.     If truckSize is less than the number of boxes of type i:
# 6.         Update ans to ans + truckSize * number of units per box of type i
# 7.         Break
# 8.     Else:
# 9.         Update ans to ans + number of boxes of type i * number of units per box of type i
# 10.        Decrement truckSize by the number of boxes of type i

# O(n⋅logn) time | O(1) space

def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
    ans = 0
    boxTypes = sorted(boxTypes, key=lambda x: x[1], reverse=True)
    for boxes, units in boxTypes:
        while boxes and truckSize > 0:
            ans += units
            boxes -= 1
            truckSize -= 1
    return ans
    

# 1196. How Many Apples Can You Put into the Basket 

# https://leetcode.com/problems/how-many-apples-can-you-put-into-the-basket/

# Description

# You have some apples, where arr[i] is the weight of the i-th apple.  You also have a basket that can carry up to 5000 units of weight.
# Return the maximum number of apples you can put in the basket.

# Pseudocode:

# 1. Sort the array
# 2. Initialize a variable ans to 0
# 3. Initialize a variable sum to 0
# 4. Iterate through the array
# 5. If sum + arr[i] <= 5000:
# 6.     Increment ans
# 7.     Update sum to sum + arr[i]
# 8. Return ans

# O(n⋅logn) time | O(1) space

def maxNumberOfApples(self, arr: List[int]) -> int:
    arr.sort()
    ans = 0
    sum = 0
    for i in range(len(arr)):
        if sum + arr[i] <= 5000:
            ans += 1
            sum += arr[i]
    return ans


# 1338. Reduce Array Size to The Half

# https://leetcode.com/problems/reduce-array-size-to-the-half/

# Description

# Given an array arr.  You can choose a set of integers and remove all the occurrences of these integers in the array.
# Return the minimum size of the set so that at least half of the integers of the array are removed.

# Pseudocode:

# 1. Count the frequency of each number
# 2. Sort the frequency array in descending order by frequency
# 3. Initialize a variable ans to 0
# 4. Initialize a variable sum to 0
# 5. Iterate through the frequency array
# 6.     Increment ans
# 7.     Update sum to sum + the current element
# 8.     If sum is greater than or equal to half the length of the array:
# 9.         Break
# 10. Return ans

# O(n⋅logn) time | O(n) space

def minSetSize(self, arr: List[int]) -> int:
    from collections import Counter
        
    freq = Counter(arr)
    length = len(arr)
    count = 0
    nums = 0
    sortedPairs = sorted(list(set(arr)), key=lambda x:freq[x], reverse=True)   
    
    for k in sortedPairs:
        
        if count + freq[k] >= length / 2:
            return nums + 1
        else:
            count += freq[k]
            nums += 1
        
    return nums