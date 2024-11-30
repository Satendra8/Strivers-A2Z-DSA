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

def postorder(root):
   """
   1. PostOrder Traversal:
   2. use 2 stacks, pop from stack1 and push to stack2
   3. if left or right node exist push in stack 1
   4. keep doing the same untill stack1 becomes empty

   PostOrder Traversal (LRN):

           1
         /    \
       2        3
      /  \     /  \
     4    5   6    7

   ans = [4 5 2 6 7 3 1]

   Time Complexity: O(N)
   Space Complexity: O(N)
   """
   if not root:
      return []

   stack1 = [root]
   stack2 = []

   while stack1:
      curr = stack1.pop()
      stack2.append(curr.data)
      if curr.left:
         stack1.append(curr.left)
      if curr.right:
         stack1.append(curr.right)
   return stack2[::-1]


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


root = Node(1)
root.left = Node(2)
root.left.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
print(postorder(root))