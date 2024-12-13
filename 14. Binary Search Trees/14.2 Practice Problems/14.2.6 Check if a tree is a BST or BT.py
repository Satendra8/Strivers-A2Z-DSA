"""
Q. Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left 
subtree
 of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

Example 1:

Input: root = [2,1,3]
Output: true
Example 2:

Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
"""

def rightMost(root):
    temp = root
    while temp.right:
        temp = temp.right
    return temp.val

def leftMost(root):
    temp = root
    while temp.left:
        temp = temp.left
    return temp.val


def isValidBST(root):
    """
    Better Approach
    1. check if root > left and root > rightmost of left subtree
    2. check if root < right and root < leftmost of right subtree
    3. keep checking for all subtree
    Time Complexity: O(N*logN)
    Space Complexity: O(1)
    """
    if not root:
        return True
    
    if root.left and (root.left.val >= root.val or rightMost(root.left) >= root.val):
        return False
    if root.right and (root.right.val <= root.val or leftMost(root.right) <= root.val):
        return False
    return isValidBST(root.left) and isValidBST(root.right)
    
INT_MIN = -2**31-1
INT_MAX = 2**31

def isValidBSTOptimal(root, min_val=INT_MIN, max_val=INT_MAX):
    """
    Optimal Approach
    1. root.val should be greater than left and less than right
    2. root.val should be lies b/w left and right val
    3. initially range will be INT_MIN and INT_MAX
    4. for left subtree max range will be root.val
    5. for right subtree min range will be root.val
    Time Complexity: O(N)
    Space Complexity: O(1)
    """
    if not root:
        return True
    if root.val >= max_val or root.val <= min_val:
        return False
    return isValidBSTOptimal(root.left, min_val, root.val) and isValidBSTOptimal(root.right, root.val, max_val)

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


root = Node(2147483647)
root.left = Node(2)
root.right = Node(2)
root.left.left = Node(2)
root.left.left.left = Node(1)
root.left.right = Node(7)

print(isValidBST(root))

