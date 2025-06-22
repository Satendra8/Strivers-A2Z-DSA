"""
Q. You are given an array arr of N integers representing a min Heap. The task is to convert it to max Heap.

A max-heap is a complete binary tree in which the value in each internal node is greater than or equal to the values in the children of that node. 

Example 1:

Input:
N = 4
arr = [1, 2, 3, 4]
Output:
[4, 2, 3, 1]
Explanation:

The given min Heap:

          1
        /   \
      2       3
     /
   4

Max Heap after conversion:

         4
       /   \
      2     3
    /
   1
Example 2:

Input:
N = 5
arr = [3, 4, 8, 11, 13]
Output:
[13, 11, 8, 3, 4]
Explanation:

The given min Heap:

          3
        /   \
      4      8
    /   \ 
  11     13

Max Heap after conversion:

          13
        /    \
      11      8
    /   \ 
   3     4
"""

""" Don't care about the input just build heap from normal array"""




def swap(arr, index1, index2):
    arr[index1], arr[index2] = arr[index2], arr[index1]
    return

def heapify(arr, i, n):
    parent = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[parent]:
        parent = left

    if right < n and arr[right] > arr[parent]:
        parent = right

    if(parent != i):
        swap(arr, parent, i)
        heapify(arr, parent, n)
    return

def buildMaxHeap(arr):
    """
    1. Don't care about the input just build heap from normal array
    Time Complexity: O(N)
    Space Complexity: O(logN) # if while loop is used in heapify then space complexity will be O(1)

    """
    n = len(arr)
    for i in range(n//2-1, -1, -1):
        heapify(arr, i, n)
    return


arr = [10,3,8,9,5,13,18,14,11,70]
buildMaxHeap(arr)
print(arr)