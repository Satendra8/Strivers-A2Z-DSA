"""
Q. Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.
A shift on s consists of moving the leftmost character of s to the rightmost position.

Example 1:
Input: s = "abcde", goal = "cdeab"
Output: true

Example 2:
Input: s = "abcde", goal = "abced"
Output: false
"""

def rotate_string(s, goal):
    """
    1. Brute Force Approach
    2. Rotate sting by 1 element each time and compare with goal
    3. if match return true, else false
    4. Time Complexity - O(N^2)
    5. Space Complexity - O(1)
    """
    n = len(s)
    for i in range(n):
        s = s[1:] + s[0]
        if s == goal:
            return True
    return False

s = "abcde"
goal = "abced"
print(rotate_string(s, goal))


def rotate_string(s, goal):
    """
    1. Optimal Approach
    2. Lenght check
    3. Concate string with itself
    4. Check if goal is in s return true, else false
    5. Time Complexity - O(N)
    6. Space Complexity - O(N)
    """

    if len(s) != len(goal):
        return False
    s = s + s # abcdeabcde
    if goal in s:
        return True
    return False

s = "abcde"
goal = "cdeab"
print(rotate_string(s, goal))