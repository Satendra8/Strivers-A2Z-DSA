"""
You are given an array of prices where prices[i] is the price of a given stock on an ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock. Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.


Example 1:
Input:
 prices = [7,1,5,3,6,4]
Output:
 5
Explanation:
 Buy on day 2 (price = 1) and 
sell on day 5 (price = 6), profit = 6-1 = 5.

Note
: That buying on day 2 and selling on day 1 
is not allowed because you must buy before 
you sell.

Example 2:
Input:
 prices = [7,6,4,3,1]
Output:
 0
Explanation:
 In this case, no transactions are 
done and the max profit = 0.
"""

def stock(arr):
    """
    Brute Force Approach
    1. loop over i to N
    2. loop over i+1 to N
    3. arr[j] - arr[i]
    4. update ans

    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """
    N = len(arr)
    ans = 0

    for i in range(N):
        for j in range(i+1, N):
            ans = max(ans, arr[j] - arr[i])
    return ans



def stockOptimal(arr):
    """
    Optimal Approach
    1. loop over array
    2. update minn if minimum number found
    3. update ans if maximum profit found

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    N = len(arr)
    minn = arr[0]
    ans = 0
    
    for num in arr:
        if num < minn:
            minn = num
        ans = max(ans, num - minn)
    return ans

arr = [7,1,5,3,6,4]
print(stockOptimal(arr))

"""
minn = 1
ans = 5
num = 4
"""