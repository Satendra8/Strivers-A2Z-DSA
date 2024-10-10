"""
Q. Given an array of integers, rotating array of elements by k elements either left or right.

Example 1:
Input: N = 7, array[] = {1,2,3,4,5,6,7} , k=2 , right
Output: 6 7 1 2 3 4 5
Explanation: array is rotated to right by 2 position.

Example 2:
Input: N = 6, array[] = {3,7,8,9,10,11} , k=3 , left 
Output: 9 10 11 3 7 8
Explanation: Array is rotated to right by 3 position.

"""

def rotate_good(arr, n, k):
    """
    Time Complexity : O(n)
    Space Complexity : O(k) // for storing temp 
    """
    k = k%n # after rotating n time the number will be same
    temp = arr[n-k:n]
    print(temp)
    arr = temp + arr[:n-k]
    return arr
    


def rotate(arr, n, k):
    """
    Time Complexity : O(n^2)
    Space Complexity : O(1)
    """
    for i in range(k):
        element = arr.pop()
        arr.insert(0, element) # O(n)
    


arr = [1,2,3,4,5,6,7]
n = 7
k = 2
rotate(arr, n, k)
print("Rotated array =======", arr)
