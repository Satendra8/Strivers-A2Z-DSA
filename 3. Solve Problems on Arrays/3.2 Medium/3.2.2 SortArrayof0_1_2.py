"""
Q. Given an array consisting of only 0s, 1s, and 2s. 
Write a program to in-place sort the array without using inbuilt sort functions. ( Expected: Single pass-O(N) and constant space)

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Input: nums = [2,0,1]
Output: [0,1,2]

Input: nums = [0]
Output: [0]

"""

def sortArray012(arr):
    """
    Brute Force Approach
    1. sort the array using bubble sort
    2. use nester for loop

    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """
    n = len(arr)
    
    for i in range(n):
        for j in range(1, n):
            if arr[j-1] > arr[j]:
                temp = arr[j]
                arr[j] = arr[j-1]
                arr[j-1] = temp
    return arr



def sortArray012Better(arr):
    """
    Better Approach
    1. get count of 0, 1 and 2
    2. form the array again with count values

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    
    lenght_0 = arr.count(0)
    lenght_1 = arr.count(1)
    lenght_2 = arr.count(2)
    
    arr = []
    arr.extend([0]*lenght_0)
    arr.extend([1]*lenght_1)
    arr.extend([2]*lenght_2)
    
    return arr


def sortArray012(arr):
    """
    Optimal Approach
    1. using Dutch National Flag Algorithm
    2. make 3 partitions
        -> [0 -> low-1]
        -> [low -> mid]
        -> [high+1 -> n-1]
    3. now array b/w [mid -> high] is unsorted
    4. Follow the following rule to sort
        a. if a[mid] == 0:
            swap mid with low
            low ++
            mid +=
        b. if a[mid] == 1:
            mid ++
        c. if a[mid] == 2:
            swap mid with high
            high --

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    n = len(arr)

    low = 0
    mid = 0
    high = n-1
    
    while mid <= high:
        
        if arr[mid] == 0:
            temp = arr[mid]
            arr[mid] = arr[low]
            arr[low] = temp
            
            low += 1
            mid += 1

        elif arr[mid] == 1:
            mid += 1

        else:
            temp = arr[mid]
            arr[mid] = arr[high]
            arr[high] = temp
            
            high -= 1
    return arr

arr = [1,1,2,1,2,1,2]
print(sortArray012(arr))