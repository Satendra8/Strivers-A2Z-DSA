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

def preorder(root):
    """
    1. PreOrder Traversal:
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

    stack = [root]

    while stack:
      curr = stack.pop()
      if curr.right:
         stack.append(curr.right)
      if curr.left:
         stack.append(curr.left)
      ans.append(curr.data)

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
print(preorder(root))