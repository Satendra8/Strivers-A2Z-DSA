"""
Q. Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

Example 1:

Input: p = [1,2,3], q = [1,2,3]
Output: true


Example 2:

Input: p = [1,2], q = [1,null,2]
Output: false


Example 3:

Input: p = [1,2,1], q = [1,1,2]
Output: false
"""

def isSameTree(p, q):
    """
    Optimal Approach
    1. Traverse each node of both
    2. Base condition: if both become null return true
    3. if only one of them become null return false
    4. if value does not match then also return null
    Time Complexity: O(N)
    Space Complexity: O(N)
    """
    if not p and not q:
        return True
    
    if not p:
        return False
    if not q:
        return False
    
    if p.val != q.val:
        return False

    return (isSameTree(p.left, q.left) and isSameTree(p.right, q.right))


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


p = Node(1)
p.left = Node(2)
p.right = Node(3)

q = Node(1)
q.left = Node(2)
q.right = Node(3)
print(isSameTree(p, q))