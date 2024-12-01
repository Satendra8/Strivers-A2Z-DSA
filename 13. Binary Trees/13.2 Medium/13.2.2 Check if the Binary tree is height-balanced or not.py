"""
Q. Given a binary tree, determine if it is height-balanced.

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: true

Example 2:

Input: root = [1,2,2,3,3,null,null,4,4]
Output: false

Example 3:

Input: root = []
Output: true
"""

def maxDepth(root):
	if root is None:
		return 0
	lh = maxDepth(root.left)
	if lh == -1:
		return -1
	rh = maxDepth(root.right)
	if rh == -1:
		return -1
	
	if abs(lh - rh) > 1:
		return -1

	return 1 + max(lh, rh)

def isBalanced(root):
	"""
	Optimal Approach
	1. find max depth of left and right node
	2. if there difference exceeds 1 return -1
	3. Edge case: at any moment if height of left and right subtree exceeds return -1
	Time Complexity: O(N)
	Space Complexity: O(logN) #auxiliary recursion stack space
	"""
	return maxDepth(root) != -1


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
print(isBalanced(root))