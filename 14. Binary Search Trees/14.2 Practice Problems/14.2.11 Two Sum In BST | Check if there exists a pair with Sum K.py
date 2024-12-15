"""
Q. Given the root of a binary search tree and an integer k, return true if there exist two elements in the BST such that their sum is equal to k, or false otherwise.

Example 1:

Input: root = [5,3,6,2,4,null,7], k = 9
Output: true

Example 2:

Input: root = [5,3,6,2,4,null,7], k = 28
Output: false
"""

def inorder(root, ans):
    if not root:
        return None
    inorder(root.left, ans)
    ans.append(root.val)
    inorder(root.right, ans)


def twoSumBrute(root, target):
    """
    Brute Force Approach
    1. get list of element using inorder traversal
    2. use 2 pointer and find the 2 sum
    Time Complexity: O(N)
    Space Complexity: O(N)
    """
    ans = []
    inorder(root, ans)
    n = len(ans)
    left = 0
    right = n - 1

    while left < right:
        if ans[left] + ans[right] == target:
            return True
        elif ans[left] + ans[right] > target:
            right -= 1
        else:
            left += 1
    return False



class BSTIteraror:
    def __init__(self, root):
        self.stack1 = []
        self.stack2 = []
        temp1 = root
        temp2 = root

        while temp1:
            self.stack1.append(temp1)
            temp1 = temp1.left

        while temp2:
            self.stack2.append(temp2)
            temp2 = temp2.right

    def next(self):
        curr = self.stack1.pop()
        root = curr.right
        while root:
            self.stack1.append(root)
            root = root.left
        return curr.val
    
    def before(self):
        curr = self.stack2.pop()
        root = curr.left
        while root:
            self.stack2.append(root)
            root = root.right
        return curr.val
    
    def hasNext(self):
        return len(self.stack1) != 0
    
    def hasBefore(self):
        return len(self.stack2) != 0


def twoSumOptimal(root, target):
    """
    Brute Force Approach
    1. create next iterator
    2. create before iterator
    3. use 2 pointer approach to find the 2 sum
    Time Complexity: O(N)
    Sapce Complexity: O(H) + O(H)
    """
    if not root:
        return False

    obj = BSTIteraror(root)
    left = obj.next()
    right = obj.before()

    while left < right:
        if left + right == target:
            return True
        elif left + right > target:
            right = obj.before()
        else:
            left = obj.next()
    return False

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

target = 21
print(twoSumOptimal(root, target))