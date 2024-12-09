"""
Q. You are given a BST(Binary Search Tree) with n number of nodes and value x. your task is to find the greatest value node of the BST which is smaller than or equal to x.
Note: when x is smaller than the smallest node of BST then returns -1.

Example:

Input:
n = 7               2
                     \
                      81
                    /     \
                 42       87
                   \       \
                    66      90
                   /
                 45
x = 87
Output:
87
Explanation:
87 is present in tree so floor will be 87.

Example 2:

Input:
n = 4                     6
                           \
                            8
                          /   \
                        7       9
x = 11
Output:
9
"""

def floor(root, x):
    """
    Iterative Approach
    1. do simple binary search
    2. if curr node val is less than target this can be ans keep storing
    Time Complexity: O(logN)
    Space Complexity: O(1)
    """
    ans = -1
    while(root):
        if root.val == x:
            return root.val
        elif root.val < x:
            ans = root.val
            root = root.right
        else:
            root = root.left
    return ans


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


root = Node(2)
root.right = Node(81)
root.right.left = Node(42)
root.right.right = Node(87)
root.right.left.right = Node(66)
root.right.left.right.left = Node(45)
root.right.right.right = Node(90)
x = 87
print(floor(root, x).val)