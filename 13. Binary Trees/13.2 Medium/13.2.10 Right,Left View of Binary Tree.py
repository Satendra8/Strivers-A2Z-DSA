"""
Q. Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example 1:

Input: root = [1,2,3,null,5,null,4]

Output: [1,3,4]

Explanation:

Example 2:

Input: root = [1,2,3,4,null,null,null,5]

Output: [1,3,4,5]

Explanation:

Example 3:

Input: root = [1,null,3]

Output: [1,3]

Example 4:

Input: root = []

Output: []
"""

def rightSideView(root):
    """
    Better Approach
    1. Use level order traversal
    2. keep updating the value of right if new found
    3. add the value rightest node for each level
    Time Complexity: O(N)
    Space Complexity: O(N)
    """
    if not root:
        return []
    
    queue = [root]
    ans = []

    while queue:
        n = len(queue)
        right = None
        for i in range(n):
            curr = queue.pop(0)

            right = curr.val
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        if right:
            ans.append(right)
    return ans


ans = []
def rightSideViewRecursive(root, height=0):
    """
    Optimal Approach
    1. Use reverse preorder (Node Right Left) NRL
    2. check if this if the first element for a index then insert it in ans
    3. first go right then left
    Time Complexity: O(N)
    Space Complexity: O(N) #little better than iterative in terms of stack space
    """
    if not root:
        return
    if len(ans) == height:
        ans.append(root.val)

    rightSideViewRecursive(root.right, height+1)
    rightSideViewRecursive(root.left, height+1)
    
    

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

root = Node(0)  # Level 0
root.left = Node(1)
root.right = Node(2)

root.left.right = Node(3)  # Level 1
root.right.left = Node(4)

root.left.right.left = Node(5)  # Level 2
root.left.right.right = Node(9)
root.right.left.right = Node(6)

root.left.right.right.right = Node(10)  # Level 3

print(rightSideView(root))
# rightSideViewRecursive(root)
# print(ans)