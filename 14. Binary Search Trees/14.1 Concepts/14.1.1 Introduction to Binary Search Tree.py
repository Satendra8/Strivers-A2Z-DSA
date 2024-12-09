"""
Q. Given an array of integers arr[] representing inorder traversal of elements of a binary tree. Return true if the given inorder traversal can be of a valid Binary Search Tree.
Note - In a valid Binary Search Tree all keys are unique.

Examples :

Input: arr[] = [8, 14, 45, 64, 100]
Output: True
Input: arr[] = [5, 6, 1, 8, 7]
Output: False
"""

def isBSTTraversal(arr):
    """
    Better Approach
    1. Just check if array is sorted or not
    Time Complexity: O(N)
    Space Complexity: O(1)
    """
    n = len(arr)
    
    for i in range(1, n):
        if arr[i-1] >= arr[i]:
            return False
    return True

arr = [8, 14, 45, 64, 100]

print(isBSTTraversal(arr))