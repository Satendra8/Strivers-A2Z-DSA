"""
Q. Given an integer i. Print the maximum number of nodes on level i of a binary tree.

Example 1:
Input: 5
Output: 16

Example 2:
Input: 1
Output: 1
"""

def countNodes(i):
    """
    return 2 ^ N-1
    Time Complexity: O(1)
    Space Complexity: O(1)
    """
    return 2 ** (i-1)

i = 1
print(countNodes(i))
