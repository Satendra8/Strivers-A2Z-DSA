def maxDepth(root, depth):
   """
   Better Approach
   1. using recursion
   2. return maximum depth between the left and right
   Time Complexity: O(N)
   Space Complexity: O(logN) #auxiliary space for recursion stack
   """
   if root is None:
      return depth

   return max(maxDepth(root.left, depth+1), maxDepth(root.right, depth+1))


def maxDepthStriver(root):
   """
   Optimal Approach
   1. using recursion
   2. return maximum depth between the left and right and add 1 for current level
   3. 1 + max(l, r)
   Time Complexity: O(N)
   Space Complexity: O(logN) #auxiliary space for recursion stack
   """
   if root is None:
      return 0
   
   return 1 + max(maxDepthStriver(root.left), maxDepthStriver(root.right))
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


root = Node(3)
root.left = Node(9)
root.right = Node(20)
root.right.left = Node(15)
root.right.right = Node(7)
print(maxDepthStriver(root))