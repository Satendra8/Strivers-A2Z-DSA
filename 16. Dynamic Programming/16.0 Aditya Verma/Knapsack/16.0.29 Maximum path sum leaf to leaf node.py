def solve(root, res):
    """
    1. base case: if root is null, height will be 0
    2. hypothesis: left node call and right node call will always return ans
    3. Induction;
        i. case 1: if current node is passing on to it's parent, will pass the best sum including itself
        ii. case 2: if current node is itself acting as root, will sum left and right including itself
        iii. update the result with maximum
        iv. return to its parent, so return temp
    """
    if not root:
        return 0

    l = solve(root.left, res)
    r = solve(root.right, res)

    temp = max(l, r) + root.val
    ans = max(temp, root.val + l + r)
    res[0] = max(res[0], ans)
    return temp

def maxPathSum(root):
    res = [-10000] # use as reference
    solve(root, res)
    return res[0] # exclude starting node

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


root = Node(-10)
root.left = Node(9)
root.right = Node(20)
# root.left.left = Node(3)
# root.left.right = Node(7)
root.right.left = Node(15)
root.right.right = Node(7)


print(maxPathSum(root))