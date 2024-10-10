"""
Q. Given a VPS represented as string s, return the nesting depth of s.
A string is a valid parentheses string (denoted VPS) if it meets one of the following:
1. It is an empty string "", or a single character not equal to "(" or ")",
2. It can be written as AB (A concatenated with B), where A and B are VPS's, or
3. It can be written as (A), where A is a VPS.

Example 1:
Input: s = "(1+(2*3)+((8)/4))+1"
Output: 3
Explanation: Digit 8 is inside of 3 nested parentheses in the string.

Example 2:
Input: s = "(1)+((2))+(((3)))"
Output: 3
"""

def max_depth(s):
    """
    1. Brute Force Approach
    2. use a list as a stack
    3. push opening bracked and pop when closing bracket comes
    4. keep check stack length and updating max depth
    5. Time Complexity - O(N)
    6. Space Complexity - O(N)
    """
    n = len(s)
    l = []
    max_depth = 0
    for i in s:
        if i == '(':
            l.append('(')
        elif i == ')':
            
            max_depth = max(len(l), max_depth)
            l.pop()
    return max_depth

s = "(1)+((2))+(((3)))"
print(max_depth(s))



def max_depth(s):
    """
    1. Optimized Approach
    2. Take a variable as a counter
    3. Increase when '(' found and decrease when ')' found
    4. keep updating the max_depth
    5. Time Complexity O(N)
    6. Space Complexity O(1)
    """
    n = len(s)
    counter = 0
    max_depth = 0
    for i in s:
        if i == '(':
            counter += 1
        elif i == ')':
            max_depth = max(counter, max_depth)
            counter -= 1
    return max_depth

s = "(1)+((2))+((3))"
print(max_depth(s))