def inorder(root):
    """
    1. InOrder Traversal:
    2. use a stack, pop last element and insert its right element then its left element
    3. do the same for all nodes
    4. if queue becomes empty that is the end of iteration

              1
            /   \
          2       3
        /  \     /  \
       4    5   6    7

    ans = [1 2 4 5 3 6 7]

    Time Complexity: O(N)
    Space Complexity: O(N)
    """

    ans = []
    if not root:
       return ans

    stack = []
    node = root

    while stack or node:
      
      if node:
         stack.append(node)
         node = node.left
      else:
         curr = stack.pop()
         ans.append(curr.data)
         node = curr.right

    return ans


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
print(inorder(root))