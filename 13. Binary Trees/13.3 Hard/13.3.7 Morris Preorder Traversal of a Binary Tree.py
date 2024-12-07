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

def preorder(root):
    """
    Morris Traversal (Threaded Binary Tree)
    1. if left -> null then print root and move left
    2. Right most guy on the left subtree point to root (thread)
    3. When come back again on the root remove the link
    4. same as inorder only one change print the root when it encounters first
    Time Complexity: O(N)
    Space Complexity: O(1)
    """
    ans = []
    curr = root

    while(curr):
        if curr.left is None:
            ans.append(curr.val)
            curr = curr.right
        else:
            prev = curr.left
            while prev.right and prev.right != curr:
                prev = prev.right

            if prev.right is None:
                prev.right = curr
                ans.append(curr.val)
                curr = curr.left
            else:
                prev.right = None
                curr = curr.right
    return ans

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


root = Node(1)
root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.right = Node(6)


print(preorder(root))