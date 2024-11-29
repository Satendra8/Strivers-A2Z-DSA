"""
Q. Given the root of a binary tree, return the postorder traversal of its nodes' values.

Example 1:

Input: root = [1,null,2,3]

Output: [3,2,1]

Explanation:


Example 2:

Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]

Output: [4,6,7,5,2,9,8,3,1]

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
    
    def postorder(self, root, ans):

        if root is None:
            return

        self.postorder(root.left, ans)
        self.postorder(root.right, ans)
        ans.append(root.val)


    def postorderTraversal(self, root):
        """
        PostOrder Traversal (LRN):

                  1
                /   \
              2       3
            /  \     /  \
           4    5   6    7

        ans = [4 5 2 6 7 3 1]

        Time Complexity: O(N)
        Space Complexity: O(N)
        """
        ans = []
        self.postorder(root, ans)
        return ans