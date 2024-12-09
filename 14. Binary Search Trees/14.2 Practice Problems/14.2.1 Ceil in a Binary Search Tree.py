"""
Q. Given a BST and a number X, find Ceil of X.
Note: Ceil(X) is a number that is either equal to X or is immediately greater than X.

If Ceil could not be found, return -1.

Example 1:

Input:
      5
    /   \
   1     7
    \
     2 
      \
       3
X = 3
Output: 3
Explanation: We find 3 in BST, so ceil
of 3 is 3.
Example 2:

Input:
     10
    /  \
   5    11
  / \ 
 4   7
      \
       8
X = 6
Output: 7
Explanation: We find 7 in BST, so ceil
of 6 is 7.
"""

def ceil(root, x):
    """
    Iterative Approach
    1. do simple binary search
    2. if curr val > x this can be answer keep storing
    Time Complexity: O(logN)
    Space Complexity: O(1)
    """
    ans = -1
    while(root):
        if root.val == x:
            return root.val
        elif root.val > x:
            ans = root.val
            root = root.left
        else:
            root = root.right
    return ans


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


root = Node(10)
root.left = Node(5)
root.right = Node(11)
root.left.left = Node(4)
root.left.right = Node(7)
root.left.right.right = Node(8)

x = 6
print(ceil(root, x))