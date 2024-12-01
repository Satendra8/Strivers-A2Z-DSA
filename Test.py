def maxDepth(root):
    if root is None:
        return 0
    return 1 + max(maxDepth(root.left), maxDepth(root.right))

def diameterOfbinaryTreeBrute(root):
    """
    Brute Force Approach
    1. visit each node
    2. count its max left height and max right height
    3. add them and update max diameter
    Time Complexity: O(N^2)
    Space Complexity: O(N)
    """
    global diameter
    if root is None:
            return 0
    lh = maxDepth(root.left)
    rh = maxDepth(root.right)
    diameter = max(diameter, lh+rh)
    diameterOfBinaryTree(root.left)
    diameterOfBinaryTree(root.right)
    return diameter



diameter = 0
def diameterOfBinaryTree(root):
    """
    Optimal Approach
    1. Use the same logic as find max Depth of of tree
    2. Tweak: keep updating the diameter with sum of left height and right height
    Time Complexity: O(N)
    Space Complexity: O(logN) #auxiliary stack space 
    """
    global diameter
    if root is None:
          return 0
    lh = diameterOfBinaryTree(root.left)
    rh = diameterOfBinaryTree(root.right)
    diameter = max(diameter, lh+rh)
    return 1 + max(lh, rh)

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
print(diameterOfbinaryTreeBrute(root))