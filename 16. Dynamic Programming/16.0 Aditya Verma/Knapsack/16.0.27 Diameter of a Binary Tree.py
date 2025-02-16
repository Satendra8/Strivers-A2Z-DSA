"""
Q. Given a binary tree, the diameter (also known as the width) is defined as the number of edges on the longest path between two leaf nodes in the tree. This path may or may not pass through the root. Your task is to find the diameter of the tree.

Examples:

Input: root[] = [1, 2, 3]

Output: 2
Explanation: The longest path has 2 edges (node 2 -> node 1 -> node 3).

Input: root[] = [5, 8, 6, 3, 7, 9]

Output: 4
Explanation: The longest path has 4 edges (node 3 -> node 8 -> node 5 -> node 6 -> node 9).
"""


def solve(root, res):
    """
    1. base case: if root is null, height will be 0
    2. hypothesis: left node call and right node call will always return ans
    3. Induction;
        i. case 1: if current node is passing on to it's parent, will pass the best count including itself
        ii. case 2: if current node is itself acting as root, will count left and right including itself
        iii. update the result with maximum
        iv. return to its parent, so return temp
    """
    if not root:
        return 0

    l = solve(root.left, res)
    r = solve(root.right, res)

    temp = max(l, r) + 1
    ans = max(temp, 1 + l + r)
    res[0] = max(res[0], ans)
    return temp

def diameter(root):
    res = [0] # use as reference
    solve(root, res)
    return res[0] - 1 # exclude starting node

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


root = Node(5)
root.left = Node(8)
root.right = Node(6)
root.left.left = Node(3)
root.left.right = Node(7)
root.right.left = Node(9)


print(diameter(root))

