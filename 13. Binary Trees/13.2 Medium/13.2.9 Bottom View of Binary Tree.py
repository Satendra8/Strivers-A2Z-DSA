"""
Q. Given a binary tree, return an array where elements represent the bottom view of the binary tree from left to right.

Note: If there are multiple bottom-most nodes for a horizontal distance from the root, then the latter one in the level traversal is considered. For example, in the below diagram, 3 and 4 are both the bottommost nodes at a horizontal distance of 0, here 4 will be considered.

                      20
                    /    \
                  8       22
                /   \     /   \
              5      3 4     25
                     /    \      
                 10       14

For the above tree, the output should be 5 10 4 14 25.

Examples :

Input:
       1
     /   \
    3     2
Output: 3 1 2
Explanation: First case represents a tree with 3 nodes and 2 edges where root is 1, left child of 1 is 3 and right child of 1 is 2.

Thus bottom view of the binary tree will be 3 1 2.
Input:
         10
       /    \
      20    30
     /  \
    40   60
Output: 40 20 60 30
Input:
        1
       /   
      2
Output: 2 1
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
            ans[col] = node.val
            if node.left:
                queue.append((node.left, col-1))
            if node.right:
                queue.append((node.right, col+1))
    return ans

def bottomView(root):
    """
    Better Approach
    0. similar to topView just keep updating if new val found for col
    1. use level order traversal
    2. initialize col=0, if for left do col-1, for right do col+1
    3. keep updating if a new val found for col
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

root = Node(20)
root.left = Node(8)
root.right = Node(22)
root.left.left = Node(5)
root.left.right = Node(3)
root.right.left = Node(4)
root.right.right = Node(25)
root.left.right.left = Node(10)
root.right.left.right = Node(14)


print(bottomView(root))