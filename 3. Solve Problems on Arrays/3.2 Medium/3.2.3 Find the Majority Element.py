"""
Q. Given an array of N integers, write a program to return an element that occurs more than N/2 times in the given array.
You may consider that such an element always exists in the array.

Example 1:
Input Format: N = 3, nums[] = {3,2,3}
Result: 3
Explanation: When we just count the occurrences of each number and compare with half of the size of the array, you will get 3 for the above solution. 

Example 2:
Input Format:  N = 7, nums[] = {2,2,1,1,1,2,2}

Result: 2

Explanation: After counting the number of times each element appears and comparing it with half of array size, we get 2 as result.

Example 3:
Input Format:  N = 10, nums[] = {4,4,2,4,3,4,4,3,2,4}

Result: 4

"""


def findMajority(arr):
    """
    Brute Force Approach
    1. Take a dict and store frequency
    2. return number with high frequency

    Time Complexity: O(n)
    Space Complexity: O(n)
    
    """
    n = len(arr)
    
    d = {}
    for i in arr:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    
    print("d==", d)
    return max(d, key=d.get)




def findMajority(arr):
    """
    Better Approach
    1. Sort the array
    2. check the number with high frequency using loop and pointer
    3. also check a condition for last element

    Time Complexity: O(nlong)
    Space Complexity: O(1)

    """
    n = len(arr)
    
    arr.sort()
    
    max_length = 0
    majority = arr[0]
    counter = 1
    
    for i in range(1,n):
        if arr[i] == arr[i-1]:
            counter += 1
        else:
            if max_length < counter:
                max_length = counter
                majority = arr[i-1]
            counter = 1

    if max_length < counter:
        max_length = counter
        majority = arr[-1]
        
    return majority


def findMajority(arr):
    """
    Optimal Approach
    1. Use Moore's Voting Algorithm
    2. Increase if same element found
    3. Decrease if different element found
    4. if count becomes 0 then, update element
    5. Need addition length check if > N/2

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    n = len(arr)
    
    counter = 1
    element = arr[0]
    
    for i in range(1, n):
        
        if counter == 0:
            element = arr[i]
        if arr[i] == element:
            counter += 1
            
        else:
            counter -= 1

    # To avoid this case [7,7,5,7,5,1,5,7,5,5,7,7,1,1,1,1]
    if arr.count(element) > n/2:
        return element
    else:
        return -1

arr = [7,7,5,7,5,1,5,7,5,5,7,7,5,5,5,5]
print(findMajority(arr))