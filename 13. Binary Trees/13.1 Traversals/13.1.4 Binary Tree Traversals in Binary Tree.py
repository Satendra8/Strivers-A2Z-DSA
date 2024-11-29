"""
Traversal Techniques (BFS)

    1. PreOrder Traversal (NLR)
    2. PostOrder Traversal (LRN)
    3. InOrder Traversal (LNR)

"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def preorder(node):
    """
    1. PreOrder Traversal (NLR):

            1
          /   \
        2       3
      /  \     /  \
     4    5   6    7

    ans = [1 2 4 5 3 6 7]

    Time Complexity: O(N)
    Space Complexity: O(N)
    """

    if node is None:
        return
    
    print(node.data, end=" ")
    preorder(node.left)
    preorder(node.right)



def postorder(node):
    """
    2. PostOrder Traversal (LRN):

                  1
                /   \
              2       3
            /  \     /  \
           4    5   6    7

    ans = [4 5 2 6 7 3 1]

    Time Complexity: O(N)
    Space Complexity: O(N)
    """
    if node is None:
        return
    
    postorder(node.left)
    postorder(node.right)
    print(node.data, end=" ")



def inorder(node):
    """
    3. InOrder Traversal (LNR):

            1
          /   \
        2       3
      /  \     /  \
     4    5   6    7

    ans = [4 2 5 1 6 3 7]

    Time Complexity: O(N)
    Space Complexity: O(N)
    """
    if node is None:
        return
    
    inorder(node.left)
    print(node.data, end=" ")
    inorder(node.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
inorder(root)