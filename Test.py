def insertIntoBST(root, val):
    """
    Iterative Approach
    1. create a node
    2. do simple binary search
    3. keep moving left if greater value found to find right place 
    4. keep moving right if smaller value found to find right place
    5. now right position found
    6. if value less than current node make left child else make right child
    Time Complexity: O(logN)
    Space Complexity: O(1)
    """
    temp = root
    node = Node(val)
    if not root:
        return node
    
    target = None
    while(temp):
        if temp.val > val:
            target = temp
            temp = temp.left
        else:
            target = temp
            temp = temp.right
    if target.val > val:
        target.left = node
    else:
        target.right = node
    return root


def insertBSTStriver(root, val):
    temp = root
    node = Node(val)
    if not root:
        return node

    while(True):
        if temp.val > val:
            if temp.left:
                temp = temp.left
            else:
                temp.left = node
                break
        else:
            if temp.right:
                temp = temp.right
            else:
                temp.right = node
                break
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


root = Node(10)
root.left = Node(5)
root.right = Node(11)
root.left.left = Node(4)
root.left.right = Node(7)
root.left.right.right = Node(8)

x = 6
r = insertBSTStriver(root, x)
inorder(r)