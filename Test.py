def rightMost(root):
    temp = root
    while temp.right:
        temp = temp.right
    return temp.val

def leftMost(root):
    temp = root
    while temp.left:
        temp = temp.left
    return temp.val


def isValidBST(root):
    if not root:
        return True
    
    if root.left and (root.left.val >= root.val or rightMost(root.left) >= root.val):
        return False
    if root.right and (root.right.val <= root.val or leftMost(root.right) <= root.val):
        return False
    return isValidBST(root.left) and isValidBST(root.right)
    
INT_MIN = -10**9
INT_MAX = 10**9

def isValidBSTOptimal(root, range=(INT_MIN, INT_MAX)):
    if not root:
        return True
    
    if root.val > range[1] or root.val < range[0]:
        return False
    return isValidBSTOptimal(root.left, (range[0], root.val)) and isValidBSTOptimal(root.right, (root.val, range[1]))

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

print(isValidBSTOptimal(root))