"""
Q. You are given an array of integers, your task is to move all the zeros in the array to the end of the array and move non-negative integers to the front by maintaining their order.

Example 1:
Input: 1 ,0 ,2 ,3 ,0 ,4 ,0 ,1
Output: 1 ,2 ,3 ,4 ,1 ,0 ,0 ,0
Explanation: All the zeros are moved to the end and non-negative integers are moved to front by maintaining order

Example 2:
Input: 1,2,0,1,0,4,0
Output: 1,2,1,4,0,0,0
Explanation: All the zeros are moved to the end and non-negative integers are moved to front by maintaining order

"""



def moveAllZeros(arr):
    """
    Time Complexity : O(n)
    Space Complexity : O(n)
    """
    counter = arr.count(0)
    temp = []
    
    for i in arr:
        if i !=0:
            temp.append(i)
    temp.extend([0]*counter)
    
    return temp


def moveAllZerosOptimized(arr):
    """
    Two Pointer Approach
    Time Complexity : O(n)
    Space Complexity : O(1)
    
    """
    j = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            
            j += 1
    return arr