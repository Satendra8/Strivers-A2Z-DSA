"""
Q. Given an array Arr[] of integers, rearrange the numbers of the given array into the lexicographically next greater permutation of numbers.

If such an arrangement is not possible, it must rearrange to the lowest possible order (i.e., sorted in ascending order).


Example 1 :

Input format:
 Arr[] = {1,3,2}
Output
: Arr[] = {2,1,3}
Explanation: 
All permutations of {1,2,3} are {{1,2,3} , {1,3,2}, {2,1,3} , {2,3,1} , {3,1,2} , {3,2,1}}. So, the next permutation just after {1,3,2} is {2,1,3}.
Example 2:

Input format:
 Arr[] = {3,2,1}
Output: 
Arr[] = {1,2,3}
Explanation: 
As we see all permutations of {1,2,3}, we find {3,2,1} at the last position. So, we have to return the topmost permutation.

"""

def next_permutation(arr):
    """
    1. Brute Force Approach
    2. Generate all possible permuation
    3. Search and find the next permutation

    Time Complexity: O(N!*N)
    Space Complexity: O(1)

    **Write Code While Leraning Recursion**
    """


def next_permutation_optimal(arr):
    """
    1. Optimal Approach
    2. Find the dip (from last check if there decreasing element)
    3. Find the nearest smallest of dip
    4. swap dip and nearest smallest

    Time Complexity: O(N)
    Space Complexity: O(1)
    """
    N = len(arr)
    dip = -1
    for i in range(N-1, 0, -1):
        if arr[i] > arr[i-1]:
            print("a")
            dip = i - 1
            break
    print(dip)
    if dip == -1:
        arr.reverse()
        print(arr)
        return

    for i in range(N-1, dip, -1):
        if arr[i] > arr[dip]:
            arr[i], arr[dip] = arr[dip], arr[i]
            break


    
    start = dip + 1
    end = N-1

    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    print(arr)


arr = [2,1,5,4,3,0,0]
# arr = [1,2,3]
next_permutation_optimal(arr)


"""
[2,3,0,0,1,4,5]
1,2,3
1,3,2
2,1,3
2,3,1
3,1,2
3,2,1


[1,3,2]

dip is 1

nearest smallest to the dip is 2

swap dip and nearest smallest 2,3,1

sort the array after dip 2,1,3 (ans)

"""
