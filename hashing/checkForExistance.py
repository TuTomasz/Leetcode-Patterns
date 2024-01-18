
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

######################################
# Additional Problems
######################################

# 217. Contains Duplicate
# 1436. Destination City
# 1496. Path Crossing

# Probelem 1 217. Contains Duplicate (Easy)

# LINK: https://leetcode.com/problems/contains-duplicate/

# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Pseudocode:

# 1. Initialize a set
# 2. Iterate through the array
# 3. Add the current element to the set
# 4. If the current element is already in the set, then return True
# 5. Return False

def containsDuplicate(nums):
    hash_set = set()
    for i in range(len(nums)):
        if nums[i] in hash_set:
            return True
        hash_set.add(nums[i])
    return False


# Problem 2 1436. Destination City (Easy)
# LINK: https://leetcode.com/problems/destination-city/

# You are given the array paths, where paths[i] = [cityAi, cityBi] means there exists a direct path going from cityAi to cityBi.
# Return the destination city, that is, the city without any path outgoing to another city.
# It is guaranteed that the graph of paths forms a line without any loop, therefore, there will be exactly one destination city.

# Pseudocode:

# 1. Initialize a set
# 2. Iterate through the array
# 3. Add the first element of the current element to the set
# 4. Iterate through the array
# 5. If the second element of the current element is not in the set, then return the second element of the current element
# 6. Return None


def destCity(paths):
    seen = set()

    for path in paths:
        seen.add(path[0])
        seen.add(path[1])

    for path in paths:

        seen.remove(path[0])

    return list(seen)[0]


# Problem 3 1496. Path Crossing (Easy)
# LINK: https://leetcode.com/problems/path-crossing/

# Given a string path, where path[i] = 'N', 'S', 'E' or 'W', each representing moving one unit north, south, east,
# or west, respectively. You start at the origin (0, 0) on a 2D plane and walk on the path specified by path.
# Return true if the path crosses itself at any point, that is, if at any time you are on a location you've previously visited.

# Pseudocode:

# 1. Initialize a set
# 2. Initialize a variable x to 0
# 3. Initialize a variable y to 0
# 4. Add (x, y) to the set
# 5. Iterate through the string
# 6. If the current character is N, then increment y
# 7. If the current character is S, then decrement y
# 8. If the current character is E, then increment x
# 9. If the current character is W, then decrement x
# 10. If (x, y) is in the set, then return True
# 11. Add (x, y) to the set
# 12. Return False

def isPathCrossing(path):
    seen = set()
    position = [0,0]
    seen.add(tuple(position))

    for c in path:
        
        if c == "N":
            position[0] += 1
        if c == "S":
            position[0] -= 1
        if c == "E":
            position[1] += 1
        if c == "W":
            position[1] -= 1

        if tuple(position) in seen:
            return True

        seen.add(tuple(position))
    
    return False