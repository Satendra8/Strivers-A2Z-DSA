"""
Q. Given an array of integers that may contain duplicates the task is to return all possible subsets. Return only unique subsets and they can be in any order.

Example 1:

Input: array[] = [1,2,2]

Output: [ [ ],[1],[1,2],[1,2,2],[2],[2,2] ]

Explanation: We can have subsets ranging from  length 0 to 3. which are listed above. Also the subset [1,2] appears twice but is printed only once as we require only unique subsets.

Input: array[] = [1]

Output: [ [ ], [1] ]

Explanation: Only two unique subsets are available
"""

def subsetSum(arr, index, ans, n, l):
    """
    1. base case: if index exceeds add it to the ans (ans is at leaf node)
    2. pick and append it to ans
    3. not pick
    4. Time Complexity: O(2^n) * l (length of ans)
    5. Space Complexity: O(2^n) * k (average length of subset)
    """
    if index >= n:
        if ans not in l:
            l.append(ans)
        return

    #pick
    subsetSum(arr, index+1, ans+[arr[index]], n, l)
    #not pick
    subsetSum(arr, index+1, ans, n, l)
    return


def subSetSumOptimized(arr, index, ans, n, l):
    """
    1. Optimal Approach
    2. sort the array for comparing prev and curr element
    3. base case: if index exceeds n return
    4. pick each element, don't consider duplicate
    5. call for each element
    6. Time Complexity: 2^t * k (where t is target, k = average lenght of ans)
    7. Space Complexity: O(k*x) (x is number of combinations)
    """
    l.append(ans)
    if index >= n:
        return

    for i in range(index, n):

        if i > index and arr[i] == arr[i-1]:
            continue
        subSetSumOptimized(arr, i+1, ans+[arr[i]], n, l)
    return

arr = [1,2,2]
arr.sort()
n = 3
l = []
subSetSumOptimized(arr, 0, [], n, l)
print(l)
