"""
Q. Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

Search for a node to remove.
If the node is found, delete the node.

Example 1:

Input: root = [5,3,6,2,4,null,7], key = 3
Output: [5,4,6,2,null,null,7]
Explanation: Given key to delete is 3. So we find the node with value 3 and delete it.
One valid answer is [5,4,6,2,null,null,7], shown in the above BST.
Please notice that another valid answer is [5,2,6,null,4,null,7] and it's also accepted.

Example 2:

Input: root = [5,3,6,2,4,null,7], key = 0
Output: [5,3,6,2,4,null,7]
Explanation: The tree does not contain a node with value = 0.

Example 3:

Input: root = [], key = 0
Output: []
"""

def helper(self, root):
        """
        1. Edge case 1: if root.left not exist return root.right and vice versa
        """
        if not root.left:
            return root.right
        if not root.right:
            return root.left
        temp =  root.left
        while(temp.right):
            temp = temp.right
        temp.right = root.right
        return root.left

def deleteNode(self, root, key):
    """
    Better Approach
    1. find node and delete
    2. Edge case 1: if root is NULL
    3. Edge case 2: If node to be deleted is root node
    4. if curr val > key and its left child val matching then
        -> helper(): move right child of current node to the extreme right of left node
        -> now curr left point to left of deleted node
    otherwise keep moving left
    5. if curr val < key and its right child val matching then
        -> helper(): move right child of current node to the extreme right of left node
        -> now curr right point to right of deleted node
    otherwise keep moving right
    Time Complexity: O(logN)
    Space Complexity: O(1)
    """
    if not root:
        return root

    if root.val == key:
        return self.helper(root)

    temp = root
    while(temp):
        if temp.val > key:
            if temp.left and temp.left.val == key:
                temp.left = self.helper(temp.left)
                break
            else:
                temp = temp.left
        else:
            if temp.right and temp.right.val == key:
                temp.right = self.helper(temp.right)
                break
            else:
                temp = temp.right
    return root

def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.val)
    inorder(root.right)


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


root = Node(5)
root.left = Node(3)
root.right = Node(6)
root.left.left = Node(2)
root.left.right = Node(4)
root.right.right = Node(7)

x = 5
r = deleteNode(root, x)
inorder(r)