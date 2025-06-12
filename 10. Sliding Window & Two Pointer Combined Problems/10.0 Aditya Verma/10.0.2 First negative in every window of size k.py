"""
Q. Given an array arr[]  and a positive integer k, find the first negative integer for each and every window(contiguous subarray) of size k.

Note: If a window does not contain a negative integer, then return 0 for that window.

Examples:

Input: arr[] = [-8, 2, 3, -6, 10] , k = 2
Output: [-8, 0, -6, -6]
Explanation:
Window [-8, 2] First negative integer is -8.
Window [2, 3] No negative integers, output is 0.
Window [3, -6] First negative integer is -6.
Window [-6, 10] First negative integer is -6.
Input: arr[] = [12, -1, -7, 8, -15, 30, 16, 28] , k = 3
Output: [-1, -1, -7, -15, -15, 0] 
Explanation:
Window [12, -1, -7] First negative integer is -1.
Window [-1, -7, 8] First negative integer is -1.
Window [-7, 8, -15] First negative integer is -7.
Window [8, -15, 30] First negative integer is -15.
Window [-15, 30, 16] First negative integer is -15.
Window [30, 16, 28] No negative integers, output is 0.
Input: arr[] = [12, 1, 3, 5] , k = 3
Output: [0, 0] 
Explanation:
Window [12, 1, 3] No negative integers, output is 0.
Window [1, 3, 5] No negative integers, output is 0.
"""

def firstNegInt(arr, k):
    """
    1. Sliding window
    2. Identification:
        i. array
        ii. sub array / sub str
        iii. window size
        iv. find first
    3. keep adding negative in an arr, add first negative in ans
    4. calculation: add negative number into negative list
    5. slide the window
    Time Complexity: O(N)
    Space Complexity: O(N)
    """
    n = len(arr)
    ans = []
    negatives = []
    i = 0
    j = 0

    while j < n:
        if arr[j] < 0:
            negatives.append(arr[j])
        if j-i+1 < k:
            j += 1
        elif j-i+1 == k:
            if not negatives:
                ans.append(0)
            else:
                ans.append(negatives[0])
                if arr[i] == negatives[0]:
                    negatives.pop(0)
            i += 1
            j += 1
    return ans


arr = [12, -1, -7, 8, -15, 30, 16, 28]
k = 3
print(firstNegInt(arr, k))

"""
arr = [-8, 2, 3, -6, 10]
k = 2
n = 5
i = 0
j = 2
ans = [-8]
negatives = [-8]

"""