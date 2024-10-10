"""
Q. Given an array, print all the elements which are leaders. A Leader is an element that is greater than all of the elements on its right side in the array.

Example 1:
Input:

 arr = [4, 7, 1, 0]
Output
:
 7 1 0
Explanation:

 Rightmost element is always a leader. 7 and 1 are greater than the elements in their right side.

Example 2:
Input:

 arr = [10, 22, 12, 3, 0, 6]
Output:

 22 12 6
Explanation:

 6 is a leader. In addition to that, 12 is greater than all the elements in its right side (3, 0, 6), also 22 is greater than 12, 3, 0, 6.

"""

def ladder(arr):
    """
    1. Brute Force Approach
    2. Select a number and check all right element of it
    3. if all elements in right are small
    4. then print answer

    Time Complexity: O(N^2)
    Space Complexity: O(1)
    """
    N = len(arr)
    
    for i in range(N):
        flag = True
        for j in range(i+1, N):
            if arr[i] < arr[j]:
                flag = False
                break
        if (flag):
            print("ans = ", arr[i])



def ladderOptimal(arr):
    """
    1. Optimal Approach
    2. Traverse from backward
    3. Track the maximum element
    4. If greater than maximun found
    5. print the number and update the maximmum

    Time Complexity: O(N^2)
    Space Complexity: O(1)
    """
    N = len(arr)

    maxx = arr[-1]
    print("ans = ", maxx)
    for i in range(N-2, 0, -1):
        if arr[i] > maxx:
            print("ans = ", arr[i])
            maxx = arr[i]


arr = [10, 22, 12, 3, 0, 6]
print(ladderOptimal(arr))