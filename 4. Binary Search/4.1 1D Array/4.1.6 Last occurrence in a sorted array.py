"""
Q. Given a sorted array of N integers, write a program to find the index of the last occurrence of the target key. If the target is not found then return -1.

Example 1:
Input: N = 7, target=13, array[] = {3,4,13,13,13,20,40}
Output: 4
Explanation: As the target value is 13 , it appears for the first time at index number 2.

Example 2:
Input: N = 7, target=60, array[] = {3,4,13,13,13,20,40}
Output: -1
Explanation: Target value 60 is not present in the array
"""



def find_last_occurance(arr, target):
    """
    1. Optimal Approach
    2. check if number match
    3. look right side to check if there is another match
    4. keep updating the ans, if match found
    5. Time Complexity: O(logN)
    6. Space Complexity: O(1)
    """
    ans = -1
    n = len(arr)
    left = 0
    right = n - 1

    while left <= right:
        mid = (left+right) // 2
        if arr[mid] > target:
            right = mid-1
        else:
            if arr[mid] == target:
                ans = mid
            left = mid+1
    return ans

arr = [3,4,12,13,13,20,40]
target = 12
print(find_last_occurance(arr, target))




def find_first_occurance(arr, target):
    """
    1. Optimal Approach
    2. Similar as lower bound
    3. check if number match
    4. look left side to check if there is another match
    5. keep updating the ans, if match found
    6. Time Complexity: O(logN)
    7. Space Complexity: O(1)
    """
    ans = -1
    n = len(arr)
    left = 0
    right = n - 1

    while left <= right:
        mid = (left+right) // 2
        if arr[mid] >= target:
            if arr[mid] == target:
                ans = mid
            right = mid-1
        else:
            left = mid+1
    return ans

arr = [3,4,12,13,13,20,40]
target = 13
print(find_first_occurance(arr, target))

# To find first and lsat occurance need to find them seperately