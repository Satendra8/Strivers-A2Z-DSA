"""
Q. The beauty of a string is the difference in frequencies between the most frequent and least frequent characters.

Example 1:

Input: s = "aabcb"
Output: 5
Explanation: The substrings with non-zero beauty are ["aab","aabc","aabcb","abcb","bcb"], each with beauty equal to 1.
Example 2:

Input: s = "aabcbaa"
Output: 17
"""

def frequency_count(substr):
    d = {}
    for i in substr:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    
    maxx = -2**31
    minn = 2**31 -1
    for v in d.values():
        maxx = max(maxx, v)
        minn = min(minn, v)

    return maxx - minn

frequency_count("abcb")

def beautySum(s):
    """
    1. Brute Force Approach
    2: Generate all possible substrigs.
    3: Pick a substring and store frequency of it's letter in a dict.
    4: Now get the maximum frequency and minimum frequeny in dict and subtract them.
    5: Add the subtracted value in answer.
    6: Do the same for all substrings.
    7. Time Complexity - O(N^3)
    8. Space Complexity - O(N)
    
    
    """
    n = len(s)
    ans = 0
    for i in range(n):
        substr = ""
        for j in range(i, n):
            substr += s[j]
            ans += frequency_count(substr)
    return ans
    

s = "aabcbaa"
print(beautySum(s))


def beautySum(s):
    """
    1. Optimal Approach
    2: Generate all possible substrigs.
    3: Store frequency of it's letter in a dict.
    4: Now get the maximum frequency and minimum frequeny in dict and subtract them.
    5: Add the subtracted value in answer.
    6. Time Complexity - O(N^2) - dictionary has max length 24 (a-z)
    7. Space Complexity - O(1)
    """
    n = len(s)
    ans = 0
    for i in range(n):
        d = {}
        for j in range(i, n):
            if s[j] in d:
                d[s[j]] += 1
            else:
                d[s[j]] = 1
            maxx = max(d.values())
            minn = min(d.values())
            ans += (maxx - minn)
    return ans
    

s = "aabcb"
print(beautySum(s))