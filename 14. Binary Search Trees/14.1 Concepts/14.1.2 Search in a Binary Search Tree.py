"""
Q. You are given the root of a binary search tree (BST) and an integer val.

Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null.

Example 1:

Input: root = [4,2,7,1,3], val = 2
Output: [2,1,3]

Example 2:

Input: root = [4,2,7,1,3], val = 5
Output: []
"""

def searchBST(root, val):
    """
    Iterative Approach
    1. Search like normal binary search
    Time Complexity: O(logN)
    Space Complexity: O(1)
    """
    while(root):
        if root.val == val:
            return root
        elif root.val > val:
            root = root.left
        else:
            root = root.right
    return None


def searchBSTRecursive(root, val):
    """
    Recursive Approach
    1. Search like normal binary search
    Time Complexity: O(logN)
    Space Complexity: O(logN)
    """
    if not root:
        return None
    
    if root.val == val:
        return root
    elif root.val > val:
        return searchBSTRecursive(root.left, val)
    else:
        return searchBSTRecursive(root.right, val)


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


root = Node(4)
root.left = Node(2)
root.right = Node(7)

root.left.left = Node(1)
root.left.right = Node(3)

val = 2
print(searchBSTRecursive(root, val))