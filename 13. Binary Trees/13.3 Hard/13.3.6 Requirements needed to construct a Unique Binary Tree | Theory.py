"""
Q. Geek wants to know the traversals required to construct a unique binary tree. Given a pair of traversal, return true if it is possible to construct unique binary tree from the given traversals otherwise return false.

Each traversal is represented with an integer: preorder - 1, inorder - 2, postorder - 3.   

Example 1:

Input:
a = 1, b=2
Output: 1
Explanation: We can construct binary tree using inorder traversal and preorder traversal. 

Example 2:

Input: a = 1, b=3
Output: 0
Explanation: We cannot construct binary tree using preorder traversal and postorder traversal. 
"""

def isPossible(a, b):
    """
    This is a theoratical question
    1. We can only construct ambiguty free tree with Inorder + Preorder/Postorder tree
    2. if tree are of same representation we can never find which one is root node
    Time Complexity: O(1)
    Space Complexity: O(1)
    """
    if a == 2 and b == 2:
        return False
    if a == 2 or b == 2:
        return True
    return False