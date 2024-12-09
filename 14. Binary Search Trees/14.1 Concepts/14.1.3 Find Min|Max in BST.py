"""
Q. Given the root of a Binary Search Tree. The task is to find the minimum valued element in this given BST.

Examples

Input: root = [5, 4, 6, 3, N, N, 7, 1]
ex-1

Output: 1
Input: root = [10, 5, 20, 2]
ex-2

Output: 2
Input: root = [10, N, 10, N, 11]
             10
              \
               10
                \
                 11
Output: 10
"""


def minValue(root):
    """
    Iterative Approach
    1. Go to the left till left exist
    Time Complexity: O(logN)
    Space Complexity: O(1)
    """
    while(root.left):
        root = root.left
    return root.val


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


root = Node(10)
root.left = Node(5)
root.right = Node(20)

root.left.left = Node(2)

print(minValue(root))