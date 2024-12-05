"""
Q. Given a Binary Tree, you need to find all the possible paths from the root node to all the leaf nodes of the binary tree.

Examples:

Input: root[] = [1, 2, 3, 4, 5]
ex-3
Output: [[1, 2, 4], [1, 2, 5], [1, 3]] 
Explanation: All possible paths: 1->2->4, 1->2->5 and 1->3
Input: root[] = [1, 2, 3]
       1
    /     \
   2       3
Output: [[1, 2], [1, 3]] 
Explanation: All possible paths: 1->2 and 1->3
Input: root[] = [10, 20, 30, 40, 60]
         10
       /    \
      20    30
     /  \
    40   60
Output: [[10, 20, 40], [10, 20, 60], [10, 30]]
Explanation: All possible paths: 10->20 ->40, 10->20->60 and 10->30
"""


def paths(root, temp, ans):
    if not root:
        return
    if not root.left and not root.right:
        temp += str(root.val)
        ans.append(list(temp))
        return
    
    temp += str(root.val)
    paths(root.left, temp, ans)
    paths(root.right, temp, ans)


def pathsArr(root, temp, ans):
    """
    Better Approach
    1. use preorder traversal
    2. use a temp array and save all visited node (don't forget to remove after visit because of pass by reference)
    3. base cases: if node is leaf node and the temp arr to final ans
    Time Complexity: O(N)
    Space Complexity: O(N)
    """
    if not root:
        return
    if not root.left and not root.right:
        temp.append(root.val)
        ans.append(temp[:]) #deep copy to avoid copying reference
        temp.pop()
        return
    
    temp.append(root.val)
    pathsArr(root.left, temp, ans)
    pathsArr(root.right, temp, ans)
    temp.pop()


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

root = Node(1)  # Level 0
root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)  # Level 1
root.left.right = Node(5)

ans = []
pathsArr(root, [], ans)
print(ans)