"""
Q. Given a sorted array, arr[] and a number target, you need to find the number of occurrences of target in arr[]. 

Examples :

Input: arr[] = [1, 1, 2, 2, 2, 2, 3], target = 2
Output: 4
Explanation: target = 2 occurs 4 times in the given array so the output is 4.
Input: arr[] = [1, 1, 2, 2, 2, 2, 3], target = 4
Output: 0
Explanation: target = 4 is not present in the given array so the output is 0.
Input: arr[] = [8, 9, 10, 12, 12, 12], target = 12
Output: 3
Explanation: target = 12 occurs 3 times in the given array so the output is 3.
"""

def findFirstOccurance(arr, target):
    low = 0
    high = len(arr) - 1
    ans = -1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            ans = mid
            high = mid - 1
        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return ans


def findLastOccurance(arr, target):
    low = 0
    high = len(arr) - 1
    ans = -1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            ans = mid
            low = mid + 1
        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return ans

def findOccurances(arr, target):
    """
    1. find first occurance
    2. find last occurance
    3. do last - first + 1
    Time Complexity: O(logN)
    Space Complexity: O(logN)
    """
    first = findFirstOccurance(arr, target)
    last = findLastOccurance(arr, target)
    if first == -1 and last == -1:
        return 0
    return last - first + 1


arr = [1, 1, 2, 2, 2, 2, 3]
target = 0
print(findOccurances(arr, target))