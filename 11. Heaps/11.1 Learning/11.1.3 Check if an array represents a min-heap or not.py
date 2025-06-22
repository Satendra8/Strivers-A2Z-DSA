"""
Q. Given an array arr of size n, the task is to check if the given array can be a level order representation of a Max Heap.

Example 1:

Input:
n = 6
arr[] = {90, 15, 10, 7, 12, 2}
Output: 
1
Explanation: 
The given array represents below tree
       90
     /    \
   15      10
  /  \     /
7    12  2
The tree follows max-heap property as every
node is greater than all of its descendants.
Example 2:
Input:  
n = 6
arr[] = {9, 15, 10, 7, 12, 11}
Output:
0
Explanation:
The given array represents below tree
       9
     /    \
   15      10
  /  \     /
7    12  11
The tree doesn't follows max-heap property 9 is
smaller than 15 and 10, and 10 is smaller than 11. 
"""

def isMaxHeap(arr):
    """
    1. For each node check if it is greater than it's child node
    Time Complexity: O(N)
    Space Complexity: O(1)
    """
    n = len(arr)

    for i in range(n):
        left = 2*i+1
        right = 2*i+2

        if left < n and arr[left] > arr[i]:
            return False
        if right < n and arr[right] > arr[i]:
            return False
    return True

arr = [9, 15, 10, 7, 12, 11]
print(isMaxHeap(arr))
