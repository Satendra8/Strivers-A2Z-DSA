"""
Q. You are given an array nodes. It contains 7 integers, which represents the value of nodes of the binary tree in level order traversal. You are also given a root of the tree which has a value equal to nodes[0].

Your task to construct a binary tree by creating nodes for the remaining 6 nodes.

Example:

Input: 
nodes = [1 2 3 4 5 6 7]
Output: 
         1
       /   \
     2       3
   /  \     /  \
   4  5    6   7
Explanation: 
The 7 node binary tree is represented above.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def createTree(root, l):
    root.left = Node(l[1])
    root.right = Node(l[2])
    root.left.left = Node(l[3])
    root.left.right = Node(l[4])
    root.right.left = Node(l[5])
    root.right.right = Node(l[6])

    return root

l = [1, 2, 3, 4, 5, 6, 7]
root = Node(1)
createTree(root, l)