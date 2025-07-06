class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right



def postorder(root):
    st = [root]
    ans = []

    while st:
        node = st.pop()
        if node.left:
            st.append(node.left)
        if node.right:
            st.append(node.right)
        ans.append(node.data)
    return ans[::-1]


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
print(postorder(root))