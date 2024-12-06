"""
Q. Given the root of a binary tree, the value of a target node target, and an integer k, return an array of the values of all nodes that have a distance k from the target node.

You can return the answer in any order.

Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
Output: [7,4,1]
Explanation: The nodes that are a distance 2 from the target node (with value 5) have values 7, 4, and 1.

Example 2:

Input: root = [1], target = 1, k = 3
Output: []
"""

def findParent(root):
    parent = {root: None}
    queue = [root]

    while queue:
        n = len(queue)
        for i in range(n):
            curr = queue.pop(0)
            if curr.left:
                parent[curr.left] = curr
                queue.append(curr.left)
            if curr.right:
                parent[curr.right] = curr
                queue.append(curr.right)
    return parent


def distanceK(root, target, k):
    """
    Better Approach
    1. find parent of all nodes using level order traversal and store in dict
    2. put the target node in queue and start traversing (level order)
    3. move left, right and upward (use parent dict)
    4. keep a visited node array, if a node is already visited don't go at that direction
    5. at any moment depth == k, remaining element in queue is ans
    Time Complexity: O(N) + O(N)
    Space Complexity: O(N) + O(N) + O(N)
    """
    parent = findParent(root)

    visited = []
    queue = [target]
    depth = 0

    while queue:
        if depth == k:
            break
        n = len(queue)
        for i in range(n):

            curr = queue.pop(0)
            visited.append(curr)

            if curr.left and curr.left not in visited:
                queue.append(curr.left)
            
            if curr.right and curr.right not in visited:
                queue.append(curr.right)
            
            if parent[curr] and parent[curr] not in visited:
                queue.append(parent[curr])
        depth += 1

    ans = []
    for node in queue:
        ans.append(node.val)
    return ans



class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


root = Node(3)  # Level 0
root.left = Node(5)
root.right = Node(1)

root.left.left = Node(6)
root.left.right = Node(2)
root.right.left = Node(0)
root.right.right = Node(8)

root.left.right.left = Node(7)
root.left.right.right = Node(4)


target = root
k = 3
print(distanceK(root, target, k))