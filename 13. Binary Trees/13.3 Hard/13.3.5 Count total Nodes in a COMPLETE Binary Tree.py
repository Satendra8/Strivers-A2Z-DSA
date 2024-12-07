"""
Q. Given the root of a complete binary tree, return the number of the nodes in the tree.
According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.
Design an algorithm that runs in less than O(n) time complexity.

Example 1:

Input: root = [1,2,3,4,5,6]
Output: 6

Example 2:

Input: root = []
Output: 0

Example 3:

Input: root = [1]
Output: 1
"""

counter = 0
def countNodes(root):
    """
    Brute Force Approach
    1. Traverse all nodes using any traversal
    2. count all nodes
    Time Complexity: O(N)
    Space Complexity: O(N) (stack space)
    """
    if not root:
        return
    global counter
    counter += 1
    countNodes(root.left)
    countNodes(root.right)


def leftHeight(root):
    height = 1
    while root.left:
        root = root.left
        height += 1
    return height

def rightHeight(root):
    height = 1
    while root.right:
        root = root.right
        height += 1
    return height

def countNodesOptimal(root):
    """
    Optimal Approach
    1. count left height and right height
    2. if both match then elements will be 2^left height - 1
    3. otherwise 1 + (find left count) + (find right count)
    Time Complexity: O(logN)^2
    Space Complexity: O(logN)
    """
    if not root:
        return 0

    lh = leftHeight(root)
    rh = rightHeight(root)

    if lh == rh:
        return 2 ** lh - 1
    else:
        return 1 + countNodesOptimal(root.left) + countNodesOptimal(root.right)

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


print(countNodesOptimal(root))