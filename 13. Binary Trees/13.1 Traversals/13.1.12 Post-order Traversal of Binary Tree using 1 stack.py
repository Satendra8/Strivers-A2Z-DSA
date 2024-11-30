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
   2. use 1 stack, use same as recursive one, go left left left..., then go right then again left left left...
   3. if leaf node add to ans, if it is right node then add root also to ans
   4. keep check left left left of right

   PostOrder Traversal (LRN):

           1
         /    \
       2        3
      /  \     /  \
     4    5   6    7

   ans = [4 5 2 6 7 3 1]

   Time Complexity: O(2N)
   Space Complexity: O(N)
   """
   if root is None:
      return []
   
   ans = []
   stack = []
   curr = root

   while stack or curr:
      #move left left left ...
      if curr:
         stack.append(curr)
         curr = curr.left
      else:
         temp = stack[-1].right
         if temp is None:
            #this is leaf node
            temp = stack.pop()
            ans.append(temp.val)

            #check if it is right node then time to return
            while stack and temp == stack[-1].right:
               temp = stack.pop()
               ans.append(temp.val)
         else:
            #need to check left for this also
            curr = temp
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
root.right.left = Node(6)
root.right.right = Node(7)
print(postorder(root))