"""
Q. Given a binary search tree and a node in it, find the in-order successor of that node in the BST.

The successor of a node p is the node with the smallest key greater than p.val.

Example 1:

Input: root = [2,1,3], p = 1

Output: 2
Explanation: 1's in-order successor node is 2. Note that both p and the return value is of TreeNode type.

Example 2:

Input: root = [5,3,6,2,4,null,null,1], p = 6
Output: null
Explanation: There is no in-order successor of the current node, so the answer is null.

"""

def inorder(root, ans):
    if not root:
        return None
    inorder(root.left, ans)
    ans.append(root.val)
    inorder(root.right, ans)


def inorderSuccesor(root, val):
    """
    Brute Force Approach
    1. form inorder arr
    2. iterate and find the first element greater than val
    Time Complexity: O(N) + O(N)
    Space Complexity: O(N)
    """
    arr = []
    inorder(root, arr)
    op = None
    for i in range(len(arr)):
        if arr[i] == val:
            break
    if i+1 < len(arr):
        op = arr[i+1]
    return op


def inorderSuccesorOptimal(root, val):
    """
    Optimal Approach
    1. if root.val found greater then val that can be possible ans
    2. keep checking for minimum possible ans
    Time Complexity: O(H) #height of BST
    Space Complexity: O(1)
    """
    ans = None

    while root:
        if root.val <= val:
            root = root.right
        else:
            ans = root.val
            root = root.left

    return ans


def inorderPredecessorOptimal(root, val):
    """
    Optimal Approach
    1. if root.val found less then val that can be possible ans
    2. keep checking for maximum possible ans
    Time Complexity: O(H) #height of BST
    Space Complexity: O(1)
    """
    ans = None

    while root:
        if root.val >= val:
            root = root.left
        else:
            ans = root.val
            root = root.right

    return ans


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

root = Node(6)
root.left = Node(2)
root.right = Node(8)
root.left.left = Node(0)
root.left.right = Node(4)
root.right.left = Node(7)
root.right.right = Node(11)
root.right.right.left = Node(10)
root.left.right.left = Node(3)
root.left.right.right = Node(5)

val = 11
print(inorderPredecessorOptimal(root, val))