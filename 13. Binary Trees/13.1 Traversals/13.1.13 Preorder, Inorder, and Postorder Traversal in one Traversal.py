"""
All Traversal in One

"""

def allorder(root):
   """
   1. PreOrder, Inorder and PostOrder Traversal all in 1:
   2. use 1 stack, to keep node and count
   3. if 1:
         +1
         preorder
         move left
      if 2:
         +1
         inorder
         move right
      if 3:
         postorder
         pop from stack

   Time Complexity: O(3N)
   Space Complexity: O(4N)
   """
   if root is None:
      return [], [], []
   
   stack = [[root, 1]]
   preorder = []
   inorder = []
   postorder = []

   while stack:
      curr = stack[-1]

      if curr[1] == 1:
         curr[1] += 1
         if curr[0].left:
            stack.append([curr[0].left, 1])
         preorder.append(curr[0].val)
      elif curr[1] == 2:
         curr[1] += 1
         if curr[0].right:
            stack.append([curr[0].right, 1])
         inorder.append(curr[0].val)
      else:
         stack.pop()
         postorder.append(curr[0].val)
   return preorder, inorder, postorder


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


root = Node(1)
root.left = Node(2)
root.right = Node(5)
root.left.left = Node(3)
root.left.right = Node(4)
root.right.left = Node(6)
root.right.right = Node(7)
print(allorder(root))