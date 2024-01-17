######################################
# Two Pointers Problems
######################################


# Problem 1: Palindrome (Easy)
# LINK: https://leetcode.com/problems/valid-palindrome/

# Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

# Pseudocode:

# 1. Initialize left and right pointers to 0 and len(s) - 1 respectively
# 2. Iterate through the string
# 3. If the current element is not alphanumeric, then increment left or decrement right
# 4. If the current elements are alphanumeric, then compare them
# 5. If they are not equal, then return False
# 6. Return True

def isPalindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:
        if not s[left].isalnum():
            left += 1
        elif not s[right].isalnum():
            right -= 1
        elif s[left].lower() != s[right].lower():
            return False
        else:
            left += 1
            right -= 1

    return True


# Problem 2: (Leetcode 392) (Easy) 
# LINK: https://leetcode.com/problems/is-subsequence/

# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none)
# of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a
# subsequence of "abcde" while "aec" is not).


# Pseudocode:

# 1. Initialize left and right pointers to 0
# 2. Iterate through the string
# 3. If the current elements are equal, then increment left and right
# 4. If not, then increment right
# 5. Return left == len(s)

def isSubsequence(s, t):
    left = 0 
    right = 0 

    while right < len(t) and left < len(s):
        
        if s[right] == t[left]:
            left += 1
        right += 1

    return left == len(s)


# Problem 3: reverse a string (Easy)
# LINK: https://leetcode.com/problems/reverse-string/

# Write a function that reverses a string. The input string is given as an array of characters s.

# Pseudocode:

# 1. Initialize left and right pointers to 0 and len(s) - 1 respectively
# 2. Iterate through the string
# 3. Swap the elements at left and right
# 4. Increment left and decrement right
# 5. Return s

def reverseString(s):
    
    left = 0
    right = len(s) - 1

    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1 
        right -= 1

    return s



# Problem 4: squares of sorted array (Easy)
# LINK: https://leetcode.com/problems/squares-of-a-sorted-array/

# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in
# non-decreasing order.

# Pseudocode:

# 1. Initialize left and right pointers to 0 and len(nums) - 1 respectively
# 2. Initialize an array of size len(nums)
# 3. Iterate through the array
# 4. If the absolute value of the element at left is greater than the absolute value of the element at right, then
#    add the square of the element at left to the result array and increment left
# 5. Else, add the square of the element at right to the result array and decrement right
# 6. Return the result array

def sortedSquares(nums):
    left = 0
    right = len(nums) - 1
    result = [0] * len(nums)

    for i in range(len(nums) - 1, -1, -1):
        if abs(nums[left]) > abs(nums[right]):
            result[i] = nums[left] * nums[left]
            left += 1
        else:
            result[i] = nums[right] * nums[right]
            right -= 1

    return result



######################################
# Two Pointers Problems
######################################

# 557 Reverse Words in a String III (Easy)
# LINK: https://leetcode.com/problems/reverse-words-in-a-string-iii/

# Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace
# and initial word order.

# Pseudocode:

# 1. Initialize left and right pointers to 0 and len(s) - 1 respectively
# 2. Iterate through the string
# 3. If the current element is a space, then reverse the substring from left to right and increment left and right
# 4. Else, increment right
# 5. Reverse the substring from left to right
# 6. Return s

def reverseWords(s):

    def reverse(word):
        word = list(word)
        left = 0
        right = len(word) - 1

        while left < right:
            word[left], word[right] = word[right], word[left]
            left += 1
            right -= 1
        
        return "".join(word)
    
    wordArr = s.split(" ")
    
    for i in range(len(wordArr)):
        wordArr[i] = reverse(wordArr[i])

    return " ".join(wordArr)


# 917 Reverse Only Letters (Easy)
# LINK: https://leetcode.com/problems/reverse-only-letters/

# Given a string s, reverse the string according to the following rules:
# All the characters that are not English letters remain in the same position.
# All the English letters (lowercase or uppercase) should be reversed.
# Return s after reversing it.

# Pseudocode:

# 1. Initialize left and right pointers to 0 and len(s) - 1 respectively
# 2. Iterate through the string
# 3. If the current element is not an alphabet, then increment left or decrement right
# 4. If the current elements are alphabets, then swap them

def reverseOnlyLetters(s):
    s = list(s)
    left = 0
    right = len(s) - 1

    while left < right:
        if not s[left].isalpha():
            left += 1
        elif not s[right].isalpha():
            right -= 1
        else:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

    return "".join(s)

# 283 Move Zeroes (Easy)

# LINK: https://leetcode.com/problems/move-zeroes/

# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero
# elements.
# Note that you must do this in-place without making a copy of the array.

# Pseudocode:

# 1. Initialize left and right pointers to 0 and len(nums) - 1 respectively
# 2. Iterate through the array
# 3. If the current element is 0, then increment left
# 4. Else, swap the elements at left and right and increment left and right
# 5. Return nums

def moveZeroes(nums):
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != 0 and nums[slow] == 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]

        # wait while we find a non-zero element to
        # swap with you
        if nums[slow] != 0:
             slow += 1
                

#2000 Reverse Prefix of Word (Easy)
        
# LINK: https://leetcode.com/problems/reverse-prefix-of-word/

# Given a 0-indexed string word and a character ch, reverse the segment of word that starts at index 0 and ends at the
# index of the first occurrence of ch (inclusive). If the character ch does not exist in word, do nothing.
# For example, if word = "abcdefd" and ch = "d", then you should reverse the segment that starts at 0 and ends at 3

# Pseudocode:
    
# 1. Initialize left and right pointers to 0 and len(word) - 1 respectively
# 2. Iterate through the string
# 3. If the current element is equal to ch, then reverse the substring from left to right and break
# 4. Else, increment right

def reversePrefix(word, ch):


    def reverse(word):
        word = list(word)
        left = 0
        right = len(word) - 1

        while left < right:
            word[left], word[right] = word[right], word[left]
            left += 1
            right -= 1

        return word
    
    idx = None

    for i in range(len(word)):
        if word[i] == ch:
            idx = i
            break

    if idx is not None:
        beg = list(word[:idx + 1])
        end = word[idx + 1:]

        beg = reverse(beg)
        return "".join(beg) + "".join(end) 
    
    return word


        



