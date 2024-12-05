def findPath(root, x, temp):
    if not root:
        return False
    
    temp.append(root)
    if root.val == x:
        return True
    
    if findPath(root.left, x, temp) or findPath(root.right, x, temp):
        return True
    temp.pop()
    return False


def lowestCommonAncestor(root, p, q):
    """
    Brute Force Approach
    1. find paths of p and q
    2. use nested loop in reverse order
    3. return first matching element in both paths 
    Time Complexity: O(2N)
    Space Complexity: O(2N)
    """
    p_path = []
    findPath(root, p, p_path)
    q_path = []
    findPath(root, q, q_path)
    
    for i in range(len(p_path)-1, -1, -1):
        for j in range(len(q_path)-1, -1, -1):
            if p_path[i].val == q_path[j].val:
                return p_path[i].val
    return -1


def lowestCommonAncestorOptimal(root, p, q):
    """
    Optimal Approach
    1. do normal traversing preorder
    2. if at any moment value found return it else return None
    3. in return value of left and right call pick the value other than None
    4. return None if left and right call both returns None
    Time Complexity: O(N)
    Space Complexity: O(N)
    """
    if not root:
        return None
    
    if root.val == p or root.val == q:
        return root
    
    l = lowestCommonAncestorOptimal(root.left, p, q)
    r = lowestCommonAncestorOptimal(root.right, p, q)

    if l and r:
        return root
    
    if l:
        return l
    
    if r:
        return r
    return None


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


root = Node(3)  # Level 0
root.left = Node(5)
root.right = Node(1)

root.left.left = Node(6)  # Level 2
root.left.right = Node(2)
root.right.left = Node(0)
root.right.right = Node(8)

root.left.right.left = Node(7)  # Level 3
root.left.right.right = Node(4)

p = 5
q = 1
print(lowestCommonAncestorOptimal(root, p, q).val)