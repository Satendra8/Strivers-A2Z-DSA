"""
Q. Given an integer N and an array of size N-1 containing N-1 numbers between 1 to N.
Find the number(between 1 to N), that is not present in the given array.

Example 1:
Input Format: N = 5, array[] = {1,2,4,5}
Result: 3
Explanation: In the given array, number 3 is missing. So, 3 is the answer.

Example 2:
Input Format: N = 3, array[] = {1,3}
Result: 2
Explanation: In the given array, number 2 is missing. So, 2 is the answer.

"""

def findMissing(arr, n):
    """
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """
    
    for i in range(1, n+1):
        if i not in arr:
            return i
            
    return -1


def findMissingBetter(arr, n):
    """
    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    new_set = set(arr)
    
    for i in range(1, n+1):
        if i not in new_set:
            return i

    return -1



def findMissingUsingDict(arr, n):
    """
    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    d = dict.fromkeys(range(1,n+1), 0)
    
    for i in arr:
        if i in d:
            d[i] += 1

    print("d", d)
    for key, value in d.items():
        if value == 0:
            return key
    return -1


def findMissingOptimal1(arr, n):
    """
    Using Summation method
    
    """
    totalSum = (n*(n+1))//2
    
    existingSum = 0
    for i in arr:
        existingSum += i
    
    return totalSum - existingSum


def findMissingOptimal2(arr, n):
    """
    Using xor
    
    1^1 = 0
    2^2 = 0
    
    1^0 = 1
    2^0 = 2
    """
    XOR1 = 0
    XOR2 = 0
    
    for i in range(1,n+1):
        XOR1 = XOR1 ^ i
    
    for i in arr:
       XOR2 = XOR2 ^ i
    
    return XOR1 ^ XOR2