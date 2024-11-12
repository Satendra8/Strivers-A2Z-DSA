"""
Q. Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.


Example 1:

Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
Example 2:

Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
Example 3:

Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.
"""

def removeKDigits(num, k):
    """
    Keep smaller one, remove larger till k becomes 0
    Edge Cases:
        i. if n == k then return 0
        ii. 0011 then trim left
        iii. if num = '12345' increasing order then no elements will be remove, remove k from last
    Time Complexity: O(N^2)
    Space Complexity: O(N)
    """
    n = len(num)
    stack = ""

    if k == 0:
        return num
    if n == k:
        return '0'
    
    i = 0
    while i < n:
        while stack and int(stack[-1]) > int(num[i]) and k > 0:
            k -= 1
            stack = stack[:-1]
        stack += num[i]
        i += 1
    if k:
        stack = stack[:len(stack)-k]
    
    stack = stack.lstrip('0')
    if not stack:
        return '0'

    return stack

num = "1173"
k = 2
print(removeKDigits(num, k))