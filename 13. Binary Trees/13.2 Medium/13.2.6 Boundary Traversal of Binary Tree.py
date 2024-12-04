"""
Q. Given a Binary Tree, perform the boundary traversal of the tree. The boundary traversal is the process of visiting the boundary nodes of the binary tree in the anticlockwise direction, starting from the root.

Example 1:
Input:Binary Tree: 1 2 7 3 -1 -1 8 -1 4 9 -1 5 6 10 11		

Output: Boundary Traversal: [1, 2, 3, 4, 5, 6, 10, 11, 9, 8, 7]
Explanation: The boundary traversal of a binary tree involves visiting its boundary nodes in an anticlockwise direction:
				
Starting from the root, we traverse from: 1
The left side traversal includes the nodes: 2, 3, 4
The bottom traversal include the leaf nodes: 5, 6, 10, 11
The right side traversal includes the nodes: 9, 8, 7
We return to the  root and the boundary traversal is complete.

Example 2:
Input:Binary Tree: 10 5 20 3 8 18 25 -1 7 -1 -1
				
Output : Boundary Traversal: [10, 5, 3, 7, 8, 18, 25, 20]
Explanation: The boundary traversal of a binary tree involves visiting its boundary nodes in an anticlockwise direction:
				
Starting from the root, we traverse from: 10
The left side traversal includes the nodes: 5
The bottom traversal include the leaf nodes: 3, 7, 8, 18, 25
The right side traversal includes the nodes: 20
We return to the  root and the boundary traversal is complete.
"""

def preorder(root, ans):
    if not root:
        return None
    
    if not root.left and not root.right:
        ans.append(root.val)

    preorder(root.left, ans)
    preorder(root.right, ans)


def leftBoundary(root):
    if not root:
        return []
    ans = []
    curr = root
    while curr:
        if curr.left or curr.right:
            ans.append(curr.val)
            curr = curr.left or curr.right
        else:
            break
    return ans


def rightBoundary(root):
    if not root:
        return []
    ans = []
    curr = root

    while curr:
        if curr.right or curr.left:
            ans.append(curr.val)
            curr = curr.right or curr.left
        else:
            break
    return ans[::-1]



def boundaryTraversal(root):
    """
    Better Approach
    1. find left boundary except leaf nodes
    2. find right boundary except leaf node in reverse order
    3. find the leaf nodes using pre order traversal
    4. combine all and return
    Time Complexity: O(logN + N + N)
    Space Complexity: O(N)
    """
    
    if not root:
        return []
    
    ans = leftBoundary(root)
    leafNodes = []
    preorder(root, leafNodes)
    ans.extend(leafNodes)
    right = rightBoundary(root.right)
    right.reverse()
    ans.extend(right)
    return ans

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


root = Node(10)
root.left = Node(5)
root.right = Node(20)
root.left.left = Node(3)
root.left.right = Node(8)
root.right.left = Node(18)
root.right.right = Node(25)
root.left.right.left = Node(7)

print(boundaryTraversal(root))
