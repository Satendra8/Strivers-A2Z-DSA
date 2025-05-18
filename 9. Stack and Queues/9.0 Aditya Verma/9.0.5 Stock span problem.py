"""
Q. The stock span problem is a financial problem where we have a series of daily price quotes for a stock and we need to calculate the span of stock price for all days. The span arr[i] of the stocks price on a given day i is defined as the maximum number of consecutive days just before the given day, for which the price of the stock on the given day is less than or equal to its price on the current day.

Examples:

Input: arr[] = [100, 80, 60, 70, 60, 75, 85]
Output: [1, 1, 1, 2, 1, 4, 6]
Explanation: Traversing the given input span 100 is greater than equal to 100 and there are no more elements behind it so the span is 1, 80 is greater than equal to 80 and smaller than 100 so the span is 1, 60 is greater than equal to 60 and smaller than 80 so the span is 1, 70 is greater than equal to 60,70 and smaller than 80 so the span is 2 and so on.  Hence the output will be 1 1 1 2 1 4 6.
Input: arr[] = [10, 4, 5, 90, 120, 80]
Output: [1, 1, 2, 4, 5, 1]
Explanation: Traversing the given input span 10 is greater than equal to 10 and there are no more elements behind it so the span is 1, 4 is greater than equal to 4 and smaller than 10 so the span is 1, 5 is greater than equal to 4,5 and smaller than 10 so the span is 2,  and so on. Hence the output will be 1 1 2 4 5 1.
"""

def calculateSpan(arr):
    """
    1. In brute force approach j depends on i
    2. use stack
    3. pattern: nearest greater to left, we have to stop when nearest greater found
    Time Complexity: O(N)
    Space Complexity: O(N)
    """
    n = len(arr)
    stack = []
    ans = []
    final_ans = []

    for i in range(n):
        if not stack:
            ans.append(-1)
        elif stack[-1][0] > arr[i]:
            ans.append(stack[-1][1])
        else:
            while stack and stack[-1][0] <= arr[i]:
                stack.pop()
            if not stack:
                ans.append(-1)
            else:
                ans.append(stack[-1][1])
        stack.append((arr[i], i))
    print(ans)
    for i in range(n):
        final_ans.append(i-ans[i])
    return final_ans


arr = [100, 80, 60, 70, 60, 75, 85]
print(calculateSpan(arr))
