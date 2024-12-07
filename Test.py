def preorder(root):
    """
    Morris Traversal (Threaded Binary Tree)
    1. if left -> null then print root and move left
    2. Right most guy on the left subtree point to root (thread)
    3. When come back again on the root remove the link
    4. same as inorder only one change print the root when it encounters first
    Time Complexity: O(N)
    Space Complexity: O(1)
    """
    ans = []
    curr = root

    while(curr):
        if curr.left is None:
            ans.append(curr.val)
            curr = curr.right
        else:
            prev = curr.left
            while prev.right and prev.right != curr:
                prev = prev.right

            if prev.right is None:
                prev.right = curr
                ans.append(curr.val)
                curr = curr.left
            else:
                prev.right = None
                curr = curr.right
    return ans

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


root = Node(1)
root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.right = Node(6)


print(preorder(root))