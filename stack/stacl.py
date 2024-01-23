# 20. Valid Parentheses

# Description:
# Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.
#

# Pseudocode:
# 1. Initialize a stack
# 2. Iterate through the string
# 3. If the current character is an opening bracket, then push it to the stack
# 4. Else, if the stack is empty or the current character is not the corresponding closing bracket of the top element of the stack, then return False
# 5. Else, pop the top element from the stack
# 6. Return True if the stack is empty, else False

def isValid(s):
    
    brackets = {')':'(','}':'{',']':'['}
    stack = []
    
    for e in s: 
    
        if e in brackets.values():
            stack.append(e)
        else:
            if stack and brackets[e] == stack[-1]:
                stack.pop()
            else:
                return False


    if len(stack) > 0:
        return False
    return True