"""
Q. Given an array of integers heights representing the histogram's bar height where the width of each bar is 1  return the area of the largest rectangle in histogram.

Example 1:

Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.


Example 2:

Input: heights = [2,4]
Output: 4
"""

def prevSmallerElement(heights, n):
    stack = []
    ans = [-1]*n

    for i in range(n):
        while stack and heights[stack[-1]] >= heights[i]:
            stack.pop()

        if stack:
            ans[i] = stack[-1]
        stack.append(i)
    return ans

def nextSmallerElement(heights, n):
    stack = []
    ans = [n]*n

    for i in range(n-1, -1, -1):
        while stack and heights[stack[-1]] >= heights[i]:
            stack.pop()

        if stack:
            ans[i] = stack[-1]
        stack.append(i)
    return ans


def largestRectangleArea(heights):
    """
    1. Find prev smaller
    2. Find next smaller
    3. do (prev + next) * heights
    4. find maximum
    Time Complexity: O(5N)
    Space Complexity: O(4N)
    """
    n = len(heights)
    maxx = 0

    prevArr = prevSmallerElement(heights, n)
    nextArr = nextSmallerElement(heights, n)

    for i in range(n):
        prev = i - prevArr[i]
        next = nextArr[i] - i
        maxx = max((prev + next - 1) * heights[i], maxx)
    return maxx

heights = [2,4]
print(largestRectangleArea(heights))