"""
Q. You are given a string num, representing a large integer. Return the largest-valued odd integer (as a string) that is a non-empty substring of num, or an empty string "" if no odd integer exists.
A substring is a contiguous sequence of characters within a string.

Example 1:

Input: num = "52"
Output: "5"
Explanation: The only non-empty substrings are "5", "2", and "52". "5" is the only odd number.
Example 2:

Input: num = "4206"
Output: ""
Explanation: There are no odd numbers in "4206".
Example 3:

Input: num = "35427"
Output: "35427"
Explanation: "35427" is already an odd number.
"""

def largest_odd_number(num):
    """
    1. Brute Force Approach
    2. Generate all substring
    3. check if sunstring is odd
    4. update the max_odd
    5. Time Compexity: O(N^3)
    6. Space Complexity: O(1)
    """
    n = len(num)
    max_odd = -1
    for i in range(n):
        for j in range(i, n):
            current_num = int(num[i:j+1])
            if current_num % 2 == 1:
                max_odd = max(max_odd, current_num)
                
    if max_odd == -1:
        return ""
    return str(max_odd)

num = "35427"
print(largest_odd_number(num))


def largest_odd_number(num):
    """
    1. Better Approach
    2. Subsequence = Prev element + curr elenent
    3. check odd and update max_odd
    4. Time Complexity: O(N^2)
    5. Space Complexity: O(1)
    """
    n = len(num)
    max_odd = -1
    for i in range(n):
        current_num = ""
        for j in range(i, n):
            current_num += num[j]
            curr = int(current_num)
            if curr % 2 == 1:
                max_odd = max(max_odd, curr)

    if max_odd == -1:
        return ""
    return str(max_odd)

num = "52"
print(largest_odd_number(num))


def largest_odd_number(num):
    """
    1. Optimal Approach
    2. Iterate from last
    3. check if last number is odd then consider from there to begining
    4. return "" in case of odd not found
    5. Time Complexity: O(N)
    6. Space Complexity: O(1)
    """
    n = len(num)
    for i in range(n-1, -1, -1):
        if int(num[i]) % 2 == 1:
            return num[:i+1]

    return ""