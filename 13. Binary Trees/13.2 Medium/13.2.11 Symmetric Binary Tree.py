"""
Q. Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

Example 1:

Input: root = [1,2,2,3,4,4,3]
Output: true

Example 2:

Input: root = [1,2,2,null,3,null,3]
Output: false
"""

def symmatry(left, right):
    if not left and not right:
        return True

    if not left:
        return False
    if not right:
        return False
    
    if left.val != right.val:
        return False
    
    return symmatry(left.left, right.right) and symmatry(left.right, right.left)

def isSymmetric(root):
    """
    Optimal Approach
    1. break the tree in 2 part left and right
    2. traverse both side simultaneously
    3. right of left is left of right and vice-versa because of mirroring (NLR <-><-> NRL)
    4. if at any moment value of both doesn't match return false
    Time Complexity: O(N)
    Space Complexity: O(N)
    """
    if not root.left and not root.right:
        return True
    return symmatry(root.left, root.right)

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

root = Node(1)  # Level 0
root.left = Node(2)
root.right = Node(2)

root.left.left = Node(3)  # Level 1
root.left.right = Node(4)
root.right.left = Node(4)
root.right.right = Node(3)

print(isSymmetric(root))