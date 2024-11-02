"""
Q. Check Balanced Parentheses. Given string str containing just the characters '(', ')', '{', '}', '[' and ']', check if the input string is valid and return true if the string is balanced otherwise return false.

Example 1:

Input: str = “( )[ { } ( ) ]”

Output: True

Explanation: As every open bracket has its corresponding 
close bracket. Match parentheses are in correct order 
hence they are balanced.
Example 2:

Input: str = “[ ( )”

Output: False

Explanation: As '[' does not have ']' hence it is 
not valid and will return false.

"""


def isValid(s):
    """
    1. Keep pushing opening brackets in stack
    2. pop if same opening bracket found
    3. Time Complexity: O(N)
    4. Space Complexity: O(N)
    """
    stack = []
    for letter in s:
        if letter == ')':
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                return False
        elif letter == ']':
            if stack and stack[-1] == "[":
                stack.pop()
            else:
                return False
        elif letter == "}":
            if stack and stack[-1] == "{":
                stack.pop()
            else:
                return False
        else:
            stack.append(letter)
    if len(stack) > 0:
        return False
    return True

s = "("
print(isValid(s))