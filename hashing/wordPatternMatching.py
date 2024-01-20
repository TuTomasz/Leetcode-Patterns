# 205. Isomorphic Strings
# 290. Word Pattern
# 791. Custom Sort String
# 1657. Determine if Two Strings Are Close


# Problem 1: 205. Isomorphic Strings (Easy)
# LINK: https://leetcode.com/problems/isomorphic-strings/

# Given two strings s and t, determine if they are isomorphic.
# Two strings s and t are isomorphic if the characters in s can be replaced to get t.
# All occurrences of a character must be replaced with another character while preserving the order of characters.
# No two characters may map to the same character, but a character may map to itself.

# Pseudocode:

# 1. Initialize a dictionary
# 2. Iterate through the strings
# 3. If the character at s[i] is not in the dictionary, then add it to the dictionary with value t[i]
# 4. Else, check if the value of s[i] in the dictionary is equal to t[i]
# 5. If not, then return False
# 6. Return True


def isIsomorphic(s, t):
    mapS = {}
    mapT = {}

    for i in range(len(s)):

        s1 = s[i]
        t1 = t[i]

        if (s1 in mapS and mapS[s1] != t1) or (t1 in mapT and mapT[t1] != s1):
            return False

        mapS[s1] = t1
        mapT[t1] = s1

    return True       


# Problem 2: 290. Word Pattern (Easy)
# LINK: https://leetcode.com/problems/word-pattern/

# Given a pattern and a string s, find if s follows the same pattern.
# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

# Pseudocode:

# 1. Initialize a dictionary
# 2. Initialize a set
# 3. Split the string into words
# 4. Iterate through the pattern
# 5. If the character at pattern[i] is not in the dictionary, then check if the current word is in the set
# 6. If it is, then return False
# 7. Else, add the character at pattern[i] to the dictionary with value current word and add the current word to the set
# 8. Else, check if the value of pattern[i] in the dictionary is equal to current word
# 9. If not, then return False
# 10. Return True


def wordPattern(pattern, s):
    a = list(pattern)
    b = s.split(" ")

    if len(a) != len(b):
        return False

    h1 = {}
    h2 = {}

    for i in range(len(a)):

        if (a[i] in h1  and h1[a[i]] != b[i]) or  (b[i] in h2  and h2[b[i]] != a[i]):

            return False
        
        h1[a[i]] = b[i]
        h2[b[i]] = a[i]

    return True
 
# Problem 3: 791. Custom Sort String (Medium)
# LINK: https://leetcode.com/problems/custom-sort-string/

# order and str are strings composed of lowercase letters. In order, no letter occurs more than once.
# order was sorted in some custom order previously. We want to permute the characters of str so that they match the
# order that order was sorted. More specifically, if x occurs before y in order, then x should occur before y in the

# Pseudocode:

# 1. Initialize a dictionary
# 2. Iterate through the string
# 3. If the character at str[i] is not in the dictionary, then add it to the dictionary with value 1
# 4. Else, increment the value of the character at str[i] in the dictionary
# 5. Initialize a string result to ""
# 6. Iterate through the order
# 7. If the character at order[i] is in the dictionary, then add the character at order[i] to result times the value
#    of the character at order[i] in the dictionary
# 8. Remove the character at order[i] from the dictionary
# 9. Iterate through the dictionary
# 10. Add the character at key times the value of the character at key to result
# 11. Return result


def customSortString(order, str):
    h = {}

    for i in range(len(str)):

        if str[i] not in h:
            h[str[i]] = 1
        else:
            h[str[i]] += 1

    result = ""

    for i in range(len(order)):

        if order[i] in h:
            result += order[i] * h[order[i]]
            del h[order[i]]

    for key in h:
        result += key * h[key]

    return result


# Problem 4: 1657. Determine if Two Strings Are Close (Medium)
# LINK: https://leetcode.com/problems/determine-if-two-strings-are-close/

# Two strings are considered close if you can attain one from the other using the following operations:
# Operation 1: Swap any two existing characters.
# For example, abcde -> aecdb
# Operation 2: Transform every occurrence of one existing character into another existing character, and do the same
# with the other character.
# For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
# You can use the operations on either string as many times as necessary.
# Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.

# Pseudocode:

# 1. Initialize a dictionary
# 2. Initialize a set
# 3. Iterate through the strings
# 4. If the character at word1[i] is not in the dictionary, then add it to the dictionary with value 1
# 5. Else, increment the value of the character at word1[i] in the dictionary
# 6. Add the character at word1[i] to the set
# 7. Iterate through the strings
# 8. If the character at word2[i] is not in the dictionary, then return False
# 9. Else, decrement the value of the character at word2[i] in the dictionary
# 10. If the value of the character at word2[i] in the dictionary is less than 0, then return False
# 11. If the character at word2[i] is not in the set, then return False
# 12. Return True


def closeStrings(word1, word2):
    if len(word1) != len(word2):
        return False

    h1 = {}
    h2 = {}
    s1 = set()

    for i in range(len(word1)):

        if word1[i] not in h1:
            h1[word1[i]] = 1
        else:
            h1[word1[i]] += 1

        s1.add(word1[i])

    for i in range(len(word2)):

        if word2[i] not in h2:
            h2[word2[i]] = 1
        else:
            h2[word2[i]] += 1

        if word2[i] not in s1:
            return False

        if h1[word2[i]] < 0:
            return False

        h1[word2[i]] -= 1

    return True
