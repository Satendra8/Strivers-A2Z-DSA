"""
Q. Given a string s consisting only of characters a, b and c.

Return the number of substrings containing at least one occurrence of all these characters a, b and c.

Example 1:

Input: s = "abcabc"
Output: 10
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" and "abc" (again). 

Example 2:

Input: s = "aaacb"
Output: 3
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "aaacb", "aacb" and "acb". 

Example 3:

Input: s = "abc"
Output: 1
"""

def numberOfSubstrings(s):
    """
    Brute Force Approach
    1. Generate all possible subarrays
    2. keep counting number of a, b and c
    3. if count_a, count_b and count_c equal or exceeds 1 count it in ans
    Time Complexity: O(N^2)
    Space Complexity: O(1)
    """
    n = len(s)
    ans = 0

    for i in range(n):
        count_a = 0
        count_b = 0
        count_c = 0
        for j in range(i, n):
            if s[j] == 'a':
                count_a += 1
            elif s[j] == 'b':
                count_b += 1
            else:
                count_c += 1

            if count_a >= 1 and count_b >= 1 and count_c >= 1:
                ans += 1
    return ans


def numberOfSubstringsBetter(s):
    """
    Better Approach
    1. Generate all possible subarrays
    2. keep counting number of a, b and c
    3. if count_a, count_b and count_c equal or exceeds 1 then take all possible subarrays of right and break
    Time Complexity: O(N^2) in worst case otherwise O(2N)
    Space Complexity: O(1)
    """
    n = len(s)
    ans = 0

    for i in range(n):
        count_a = 0
        count_b = 0
        count_c = 0
        print("ans=", ans)
        for j in range(i, n):
            if s[j] == 'a':
                count_a += 1
            elif s[j] == 'b':
                count_b += 1
            else:
                count_c += 1

            if count_a >= 1 and count_b >= 1 and count_c >= 1:
                ans += (n - j)
                break
    return ans


def numberOfSubstringsOptimal(s):
    """
    Optimal Approach
    1. keep updating indexes
    2. find sub array which has atleast all elements at least once
    3. take the smallest index and look at left
    4. add up all possible subarrays of left
    Time Complexity: O(N)
    Space Complexity: O(3)
    """
    n = len(s)
    ans = 0
    d = [-1,-1,-1]

    for right in range(n):
        d[ord(s[right]) - 97] = right

        if -1 not in d:
            mini = min(d)
            ans += (mini - 0 + 1)
    return ans


s = "abc"
print(numberOfSubstringsOptimal(s))



def count(s):
    """
    Sliding Window
    Pattern: Atmost - Atleast
    Identification: not sure whether to move i or j
    Find for len <= 3, this is derived by n * (n+1) // 2
    Then for len <= 2, then subtract to get answer
    """
    n = len(s)
    i = 0
    j = 0
    d = {}
    ans = 0

    while j<n:
        if s[j] in d:
            d[s[j]] += 1
        else:
            d[s[j]] = 1
        
        if len(d) > 2:
            while len(d) > 2:
                d[s[i]] -= 1
                if d[s[i]] == 0:
                    del d[s[i]]
                i += 1
        ans += (j-i+1)
        j += 1
    return ((n * (n+1)) // 2) - ans
        

s = "abbbbbb"
print(count(s))