# 1768. Merge Strings Alternately (Easy)

# LINK: https://leetcode.com/problems/merge-strings-alternately/

# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.
# Return the merged string.

# Pseudocode:

# 1. Initialize a string ans to ""
# 2. Initialize two pointers i and j to 0
# 3. Iterate through the strings
# 4. Add the character at word1[i] to ans
# 5. Add the character at word2[j] to ans
# 6. Increment i and j
# 7. Iterate through the remaining characters in word1
# 8. Add the character at word1[i] to ans
# 9. Increment i
# 10. Iterate through the remaining characters in word2
# 11. Add the character at word2[j] to ans
# 12. Increment j
# 13. Return ans


def mergeAlternately(self, word1, word2):
    
    ans = ""
    i = 0
    j = 0
    
    while i < len(word1) and j < len(word2):
        
        ans += word1[i]
        ans += word2[j]
        i += 1
        j += 1
        
    while i < len(word1):
        ans += word1[i]
        i += 1
    
    while j < len(word2):
        ans += word2[j]
        j += 1