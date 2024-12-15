"""
Q. Implement the BSTIterator class that represents an iterator over the in-order traversal of a binary search tree (BST):

BSTIterator(TreeNode root) Initializes an object of the BSTIterator class. The root of the BST is given as part of the constructor. The pointer should be initialized to a non-existent number smaller than any element in the BST.
boolean hasNext() Returns true if there exists a number in the traversal to the right of the pointer, otherwise returns false.
int next() Moves the pointer to the right, then returns the number at the pointer.
Notice that by initializing the pointer to a non-existent smallest number, the first call to next() will return the smallest element in the BST.

You may assume that next() calls will always be valid. That is, there will be at least a next number in the in-order traversal when next() is called.

Example 1:

Input
["BSTIterator", "next", "next", "hasNext", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
[[[7, 3, 15, null, null, 9, 20]], [], [], [], [], [], [], [], [], []]
Output
[null, 3, 7, true, 9, true, 15, true, 20, false]

Explanation
BSTIterator bSTIterator = new BSTIterator([7, 3, 15, null, null, 9, 20]);
bSTIterator.next();    // return 3
bSTIterator.next();    // return 7
bSTIterator.hasNext(); // return True
bSTIterator.next();    // return 9
bSTIterator.hasNext(); // return True
bSTIterator.next();    // return 15
bSTIterator.hasNext(); // return True
bSTIterator.next();    // return 20
bSTIterator.hasNext(); // return False
"""

def inorder(root):
    """
    Brute Force Approach
    1. use yeild operator to make generator
    Time Complexity: O(N)
    Sapce Complexity: O(N)
    """
    if not root:
        return None
    yield from inorder(root.left)
    yield root.val
    yield from inorder(root.right)


class BSTIterator:
    """
    Optimal Approach
    1. take a stack and initialize by pushing all left's
    2. when calling next function pop element from stack push all left of it's right
    3. return the value of current node as ans
    Time Complexity: O(1)
    Space Complexity: O(H)
    """
    def __init__(self, root):
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    def next(self):
        ans = self.stack.pop()
        if ans.right:
            root = ans.right
            while root:
                self.stack.append(root)
                root = root.left
        return ans.val

    def hasNext(self):
        return len(self.stack) != 0

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


root = Node(7)
root.left = Node(3)
root.right = Node(10)

# Left subtree
root.left.left = Node(2)
root.left.right = Node(6)
root.left.left.left = Node(1)
root.left.right.left = Node(5)
root.left.right.left.left = Node(4)

# Right subtree
root.right.left = Node(9)
root.right.left.left = Node(8)
root.right.right = Node(12)
root.right.right.right = Node(14)


obj = BSTIterator(root)
print(obj.next())
print(obj.next())
print(obj.next())
print(obj.next())
print(obj.next())
print(obj.next())
print(obj.next())
print(obj.next())
print(obj.next())
print(obj.next())
print(obj.next())
print(obj.next())
print(obj.hasNext())