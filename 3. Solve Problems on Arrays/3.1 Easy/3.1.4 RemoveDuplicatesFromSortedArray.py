"""
Q.  Given an integer array sorted in non-decreasing order, remove the duplicates in place such that each unique element appears only once. The relative order of the elements should be kept the same.

Note: Return k after placing the final result in the first k slots of the array.

Example 1: 

Input: arr[1,1,2,2,2,3,3]

Output: arr[1,2,3,_,_,_,_]

Explanation: Total number of unique elements are 3, i.e[1,2,3] and Therefore return 3 after assigning [1,2,3] in the beginning of the array.

Example 2: 

Input: arr[1,1,1,2,2,3,3,3,3,4,4]

Output: arr[1,2,3,4,_,_,_,_,_,_,_]

Explanation: Total number of unique elements are 4, i.e[1,2,3,4] and Therefore return 4 after assigning [1,2,3,4] in the beginning of the array.

"""

def removeDuplicate(arr):
    """
    Time Complexity : O(n)
    Space Complexity : O(n) // for storing temp
    """
    n = len(arr)

    prev = arr[0]
    temp = [prev]
    
    for i in range(1, n):
        if arr[i] != prev:
            prev = arr[i]
            temp.append(arr[i])
            
    return temp


def removeDuplicatesOptimized(arr):
    """
    1. 
    Time Complexity : O(n)
    Space Complexity : O(1)
    """
    n = len(arr)
    
    prev = arr[0]
    index = 1
    counter = 1
    for i in range(1, n):
        if arr[i] > prev:
            prev = arr[i]
            temp = arr[i]
            arr[i] = arr[index]
            arr[index] = temp
            index += 1
            counter += 1

    print("Counter", counter)
    return arr
            
print(removeDuplicatesOptimized([1,2,3,4,4,4,4,5,5,5,5]))