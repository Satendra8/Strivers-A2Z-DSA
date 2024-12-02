def zigzagLevelOrder(root):
    """
    Better Approach
    1. Do level order traversal
    2. tweak: alternatively reverse the level nodes before inserting to ans
    Time Complexity: O(N)
    Space Complexity: O(N)
    """
    if not root:
        return []
    
    ans = []
    queue = [root]
    flip = False

    while queue:
        n = len(queue)
        temp = []

        for i in range(n):
            curr = queue.pop(0)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
            temp.append(curr.val)
        if flip:
            temp.reverse()
        flip = not flip
        ans.append(temp)
    return ans

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


root = Node(3)
root.left = Node(9)
root.right = Node(20)
root.right.left = Node(15)
root.right.right = Node(7)
print(zigzagLevelOrder(root))