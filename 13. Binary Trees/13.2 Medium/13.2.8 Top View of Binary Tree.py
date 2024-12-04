"""
Q. You are given a binary tree, and your task is to return its top view. The top view of a binary tree is the set of nodes visible when the tree is viewed from the top.

Note: 

Return the nodes from the leftmost node to the rightmost node.
If two nodes are at the same position (horizontal distance) and are outside the shadow of the tree, consider the leftmost node only. 
Examples:

Input: root[] = [1, 2, 3] 
      1
    /   \
   2     3
Output: [2, 1, 3]
Input: root[] = [10, 20, 30, 40, 60, 90, 100]
       10
    /      \
   20       30
 /   \    /    \
40   60  90    100
Output: [40, 20, 10, 30, 100]
Explaination: 
The root 10 is visible.
On the left, 40 is the leftmost node and visible, followed by 20.
On the right, 30 and 100 are visible. Thus, the top view is 40 20 10 30 100.
Input: root[] = [1,2,3,N,4,N,N,N,5,N,6]
       1
     /   \
    2     3
     \   
      4
       \
        5
         \
          6
Output: [2, 1, 3, 6]
Explaination: 
Node 1 is the root and visible.
Node 2 is the left child and visible from the left side.
Node 3 is the right child and visible from the right side.
Nodes 4, 5, and 6 are vertically aligned, but only the lowest node 6 is visible from the top view. Thus, the top view is 2 1 3 6.
"""

def levelOrder(root):
    if not root:
        return

    queue = [(root, 0)]
    ans = {}

    while queue:
        n = len(queue)
        for i in range(n):
            curr = queue.pop(0)
            node = curr[0]
            col = curr[1]
            if col not in ans:
                ans[col] = node.val
            if node.left:
                queue.append((node.left, col-1))
            if node.right:
                queue.append((node.right, col+1))
    return ans

def topView(root):
    """
    Better Approach
    1. use level order traversal
    2. initialize col=0, if for left do col-1, for right do col+1
    3. if col is not in dict insert first value of that
    4. sort the ans dict by key
    5. form list of values and return
    Time Complexity: O(N) + logN
    Space Complexity: O(N) + logN
    """
    ans = levelOrder(root)
    final_ans = []
    for key,val in sorted(ans.items()):
        final_ans.append(val)
    return final_ans

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

root = Node(1)
root.left = Node(2)
root.right = Node(3)

print(topView(root))