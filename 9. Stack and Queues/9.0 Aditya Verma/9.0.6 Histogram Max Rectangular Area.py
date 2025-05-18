"""
Q. You are given a histogram represented by an array arr, where each element of the array denotes the height of the bars in the histogram. All bars have the same width of 1 unit.

Your task is to find the largest rectangular area possible in the given histogram, where the rectangle can be formed using a number of contiguous bars.

Examples:

Input: arr[] = [60, 20, 50, 40, 10, 50, 60]
 Largest-Rectangular-Area-in-a-Histogram
Output: 100
Explanation: We get the maximum by picking bars highlighted above in green (50, and 60). The area is computed (smallest height) * (no. of the picked bars) = 50 * 2 = 100.
Input: arr[] = [3, 5, 1, 7, 5, 9]
Output: 15
Explanation:  We get the maximum by picking bars 7, 5 and 9. The area is computed (smallest height) * (no. of the picked bars) = 5 * 3 = 15.
Input: arr[] = [3]
Output: 3
Explanation: In this example the largest area would be 3 of height 3 and width 1.
"""

def NSR(arr, n):
    """
    pattern: nearest smaller to right
    push n if stack is empty as right most
    """
    stack = []
    ans = []

    for i in range(n-1, -1, -1):
        if not stack:
            ans.append(n)
        elif stack[-1][0] < arr[i]:
            ans.append(stack[-1][1])
        else:
            while stack and stack[-1][0] >= arr[i]:
                stack.pop()
            if not stack:
                ans.append(n)
            else:
                ans.append(stack[-1][1])
        stack.append((arr[i], i))
    ans.reverse()
    return ans


def NSL(arr, n):
    """
    pattern: nearest smaller to right
    push -1 if stack is empty as left most
    """
    stack = []
    ans = []

    for i in range(n):
        if not stack:
            ans.append(-1)
        elif stack[-1][0] < arr[i]:
            ans.append(stack[-1][1])
        else:
            while stack and stack[-1][0] >= arr[i]:
                stack.pop()
            if not stack:
                ans.append(-1)
            else:
                ans.append(stack[-1][1])
        stack.append((arr[i], i))
    return ans

def getMaxArea(arr):
    """
    1. Building can be expended into other building if other building >= current building
    2. Find nearest smaller to right
    3. Find nearest smaller to left
    3. Find width = right[i] - left[i] - 1
    4. area =  widht[i] * arr[i]
    5. return max of area
    """
    n = len(arr)
    right = NSR(arr, n)
    left = NSL(arr, n)
    width = []

    for i in range(n):
        width.append(right[i]-left[i]-1)
    area = []
    for i in range(n):
        area.append(width[i]*arr[i])
    return max(area)


arr = [347, 411, 476, 253, 314, 495, 959, 158, 541]
print(getMaxArea(arr))