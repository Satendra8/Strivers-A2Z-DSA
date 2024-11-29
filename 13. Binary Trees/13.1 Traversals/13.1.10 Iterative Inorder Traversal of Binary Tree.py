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

def inorder(root):
    """
    1. InOrder Traversal:
    2. use a stack, pop last element and insert its right element then its left element
    3. do the same for all nodes
    4. if queue becomes empty that is the end of iteration

              1
            /   \
          2       3
        /  \     /  \
       4    5   6    7

    ans = [1 2 4 5 3 6 7]

    Time Complexity: O(N)
    Space Complexity: O(N)
    """

    ans = []
    if not root:
       return ans

    stack = []
    node = root

    while stack or node:
      
      if node:
         stack.append(node)
         node = node.left
      else:
         curr = stack.pop()
         ans.append(curr.data)
         node = curr.right

    return ans


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
print(inorder(root))