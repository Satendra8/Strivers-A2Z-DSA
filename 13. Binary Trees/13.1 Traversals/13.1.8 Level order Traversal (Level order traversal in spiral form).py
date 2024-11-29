"""
Q. Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []

"""

def levelOrder(root):
    """
    1. Level Order Traversal (BFS):
    2. use a queue, pop all nodes at a level, push all childs of all nodes
    3. do the same for all nodes
    4. if queue becomes empty that is the end of iteration

              1
            /   \
          2       3
        /  \     /  \
       4    5   6    7

    ans = [1 2 3 4 5 6 7]

    Time Complexity: O(N)
    Space Complexity: O(2N)
    """
    ans = []
    if not root:
       return ans

    queue = [root]

    while queue:
      n = len(queue)
      temp = []

      for i in range(n):
          curr = queue.pop(0)
          if curr.left:
            queue.append(curr.left)
          if curr.right:
            queue.append(curr.right)
          temp.append(curr.data)
      ans.append(temp)
    return ans


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
print(levelOrder(root))