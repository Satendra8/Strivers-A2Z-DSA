"""
Q. Given the root of a binary tree, return the preorder traversal of its nodes' values.

Example 1:

Input: root = [1,null,2,3]

Output: [1,2,3]

Explanation:



Example 2:

Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]

Output: [1,2,4,5,6,7,3,8,9]

Explanation:


Example 3:

Input: root = []

Output: []

Example 4:

Input: root = [1]

Output: [1]

"""

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def preorder(self, root, ans):
        if root is None:
            return
    
        ans.append(root.val)
        self.preorder(root.left, ans)
        self.preorder(root.right, ans)

    def preorderTraversal(self, root):
        """
        1. PreOrder Traversal (NLR)

        Time Complexity: O(N)
        Space Complexity: O(N)
        """
        ans = []
        self.preorder(root, ans)
        return ans