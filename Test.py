def countNodes(i):
    """
    return 2 ^ N-1
    Time Complexity: O(1)
    Space Complexity: O(1)
    """
    return 2 ** (i-1)

i = 1
print(countNodes(i))


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
