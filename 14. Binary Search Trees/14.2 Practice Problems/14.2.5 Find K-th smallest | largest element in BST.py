"""
Q. Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

Example 1:

Input: root = [3,1,4,null,2], k = 1
Output: 1

Example 2:

Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3
"""

def preorder(root, ans):
    if not root:
        return
    ans.append(root.val)
    if root.left:
        preorder(root.left, ans)
    if root.right:
        preorder(root.right, ans)


def findKthSmallest(root, k):
    """
    Brute Force Approach
    1. use any traversal
    2. form array
    3. sort array
    4. return kth
    Time Complexity: O(NlogN)
    Space Complexity: O(N) 
    """
    ans = []
    preorder(root, ans)
    ans.sort()
    return ans[k-1]



def inorder(root, k):
    """
    Better Approach
    1. Do inorder traversal (for BST inorder traversal gives sorted order output)
    2. keep decrementing the k until it becomes 0
    3. the moment when k becomes 0 that is the ans
    Time Complexity: O(N)
    Space Complexity: O(N)
    """
    stack = []
    curr = root

    while stack or curr:
        if curr:
            stack.append(curr)
            curr = curr.left
        else:
            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val
            curr = curr.right
    return -1


def findKthElement(root, k):
    """
    Optimal Approach
    1. use inorder traversal
    2. use morris algorithm to reduce the space complexity
        -> if left is None print curr and move right
        -> right most of left will point to curr, if already pointing then remove link
    3. keep reducing the k, when it becomes 0 return root
    Time Complexity: O(N)
    Space Complexity: O(1)
    """
    curr = root
    while curr:
        if curr.left is None:
            k -= 1
            if k == 0:
                return curr.val
            curr = curr.right
        else:
            prev = curr.left
            while prev.right and prev.right != curr:
                prev = prev.right

            if prev.right:
                prev.right = None
                k -= 1
                if k == 0:
                    return curr.val
                curr = curr.right
            else:
                prev.right = curr
                curr = curr.left
    return -1

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


root = Node(5)
root.left = Node(3)
root.right = Node(6)
root.left.left = Node(2)
root.left.left.left = Node(1)
root.left.right = Node(4)

k = 1
print(findKthElement(root, k))