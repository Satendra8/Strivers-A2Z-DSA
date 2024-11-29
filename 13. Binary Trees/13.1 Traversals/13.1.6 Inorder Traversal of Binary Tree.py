"""
Q. Given the root of a binary tree, return the inorder traversal of its nodes' values.

Example 1:

Input: root = [1,null,2,3]

Output: [1,3,2]

Explanation:

Example 2:

Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]

Output: [4,2,6,5,7,1,3,9,8]

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
    def inorder(self, root, ans):
        if root is None:
            return

        self.inorder(root.left, ans)
        ans.append(root.val)
        self.inorder(root.right, ans)


    def inorderTraversal(self, root):
        """
        InOrder Traversal (LNR):

                  1
                /   \
              2       3
            /  \     /  \
           4    5   6    7

        ans = [4 2 5 1 6 3 7]

        Time Complexity: O(N)
        Space Complexity: O(N)
        """
        ans = []
        self.inorder(root, ans)
        return ans
        