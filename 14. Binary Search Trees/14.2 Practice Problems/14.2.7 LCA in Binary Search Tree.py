"""
Q. Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Example 1:

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.
Example 2:

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
Example 3:

Input: root = [2,1], p = 2, q = 1
Output: 2
"""

def findPath(root, x):
    if not root:
        return []
    ans = []

    while root:
        ans.append(root.val)
        if root.val == x:
            return ans
        elif root.val > x:
            root = root.left
        else:
            root = root.right
    return ans 


def LCA(root, p, q):
    """
    Brute Force Approach
    1. find the path to reach p
    2. find the path to reach q
    3. iterate from last if both matches return
    Time Complexity: O(logN + logN + N)
    Space Complexity: O(N)
    """
    p_list = findPath(root, p)
    q_list = findPath(root, q)

    for i in range(len(p_list)-1, -1, -1):
        for j in range(len(q_list)-1, -1, -1):
            if p_list[i] == q_list[j]:
                return p_list[i]
    return -1


def LCABetter(root, p, q):
    """
    Better Approach
    1. Traverse in both direction
    2. if p or q found return
    3. while returning b/w null and val choose val to return
    4. if both value found, it means that node is lca return it
    Time Complexity: O(N)
    Space Complexity: O(logN) #stack space
    """
    if not root:
        return None
    
    if root.val == p or root.val == q:
        return root.val
    
    x = LCABetter(root.left, p, q)
    y = LCABetter(root.right, p, q)

    if x is not None and y is not None:
        return root.val
    if x is not None:
        return x
    if y is not None:
        return y
    return None


def LCAOptimal(root, p, q):
    """
    Optimal Approach
    1. At the moment when p and q lies on left and right side, that is the lca
    2. move left if p and q are less than node val
    3. move right if p and q are greater than node val
    Time Complexity: O(logN)
    Space Complexity: O(1)
    """
    while root:
        if root.val > p and root.val > q:
            root = root.left
        elif root.val < p and root.val < q:
            root = root.right
        else:
            return root.val
    return root

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
root.right.right = Node(9)
root.left.right.left = Node(3)
root.left.right.right = Node(5)

p = 2
q = 4
print(LCAOptimal(root, p, q))