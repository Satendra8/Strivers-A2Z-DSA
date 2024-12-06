"""
Q. Given the root of a binary tree, return the maximum width of the given tree.

The maximum width of a tree is the maximum width among all levels.

The width of one level is defined as the length between the end-nodes (the leftmost and rightmost non-null nodes), where the null nodes between the end-nodes that would be present in a complete binary tree extending down to that level are also counted into the length calculation.

It is guaranteed that the answer will in the range of a 32-bit signed integer.

Example 1:

Input: root = [1,3,2,5,3,null,9]
Output: 4
Explanation: The maximum width exists in the third level with length 4 (5,3,null,9).

Example 2:

Input: root = [1,3,2,5,null,null,9,6,null,7]
Output: 7
Explanation: The maximum width exists in the fourth level with length 7 (6,null,null,null,null,null,7).

Example 3:

Input: root = [1,3,2,5]
Output: 2
Explanation: The maximum width exists in the second level with length 2 (3,2).
"""

def widthOfBinaryTree(root):
    """
    Better Approach
    1. Basic idea is if we assign index to each node (Use Level Order Traversal)
    2. using formula for left node = 2*i+1, right node = 2*i+2 (where i=index of curr node)
    3. if we keep doing 2*i+1 the number will become huge so doing index - index of left most element
    4. keep update the width with maximum (max_at_level - min_at_level + 1)
    Time Complexity: O(N)    
    Space Complexity: O(N)
    """
    queue = [(root, 0)]
    width = 0

    while queue:
        n = len(queue)
        min_at_level = queue[0][1]
        max_at_level = queue[-1][1]

        width = max(width, max_at_level - min_at_level + 1)

        for i in range(n):
            curr = queue.pop(0)
            node = curr[0]
            index = curr[1]
            index = index - min_at_level
            if node.left:
                queue.append((node.left, 2 * index + 1))
            if node.right:
                queue.append((node.right, 2 * index + 2))
    return width


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


root = Node(1)  # Level 0
root.left = Node(3)
root.right = Node(7)

root.left.left = Node(8)  # Level 2
root.right.right = Node(4)

print(widthOfBinaryTree(root))