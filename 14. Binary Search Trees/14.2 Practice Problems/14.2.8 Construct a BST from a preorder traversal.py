"""
Q. Given an array of integers preorder, which represents the preorder traversal of a BST (i.e., binary search tree), construct the tree and return its root.

It is guaranteed that there is always possible to find a binary search tree with the given requirements for the given test cases.

A binary search tree is a binary tree where for every node, any descendant of Node.left has a value strictly less than Node.val, and any descendant of Node.right has a value strictly greater than Node.val.

A preorder traversal of a binary tree displays the value of the node first, then traverses Node.left, then traverses Node.right.

Example 1:

Input: preorder = [8,5,1,7,10,12]
Output: [8,5,10,1,7,null,12]

Example 2:

Input: preorder = [1,3]
Output: [1,null,3]
"""

def bstFromPreorder(arr):
    """
    Brute Force Approach
    1. make first element as root node
    2. find correct position by moving left and right
    3. keep track of prev node
    4. if leaf found
    5. check if element is less create node and assing to left
    6. check if element is greater create node and assing to right
    Time Complexity: O(N*N)
    Space Complexity: O(1)
    """
    root = Node(arr[0])

    for i in range(1, len(arr)):
        temp = root
        curr = None
        while temp:
            curr = temp
            if temp.val > arr[i]:
                temp = temp.left
            else:
                temp = temp.right

        if curr.val > arr[i]:
            curr.left = Node(arr[i])
        else:
            curr.right = Node(arr[i])
    return root


def bstFromPreorderBetter(arr):
    """
    Better Approach
    1. Sort the array and get inorder
    2. now we have preorder and inorder
    3. construct binary tree using inorder and preorder
    Time Complexity: O(Nlogn) + O(N)
    Space Complexity: O(N)
    """
    inorder = sorted(arr)
    # construct binary tree using preorder and inorder

def bstFromPreorderOptimal(preorder, upper_bound=2**31, index=None):
    """
    Optimal Approach
    1. initialize the upper bound as infinite
    2. if value at index lies inside upper bound create node and find its left and right
    3. if value does not in upper bound return None
    4. Base case: if done for all arr elements return None
    Time Complexity: O(3) # visiting each node 3 times
    Space Complexity: O(1)
    """
    if not index:
        index = [0]
    if index[0] == len(preorder):
        return None
    
    if preorder[index[0]] < upper_bound:
        root = Node(preorder[index[0]])
        index[0] += 1
        root.left = bstFromPreorderOptimal(preorder, root.val, index)
        root.right = bstFromPreorderOptimal(preorder, upper_bound, index)
        return root
    return None
    



def inorder(root):
    if not root:
        return root
    inorder(root.left)
    print(root.val, end=" ")
    inorder(root.right)
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# arr = [8,5,1,7,10,12]
arr = [1,3]
root = bstFromPreorderOptimal(arr)
inorder(root)