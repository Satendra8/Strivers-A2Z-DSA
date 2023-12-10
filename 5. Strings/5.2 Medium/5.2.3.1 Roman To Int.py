"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Example 1:

Input: s = "III"
Output: 3
Explanation: III = 3.
Example 2:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 3:

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
"""


def romanToInt(self, s: str) -> int:
    """
    1. Brute Force Approach
    2. Iterate over each charachter and get their value and add
    3. In case of IV, IX ..... increment by 2
    4. Time Complexity - O(N)
    5. Space Complexity - O(1)
    """
    ans = 0
    d = {"I": 1, "V":5, "X":10, "L":50, "C":100, "D":500, "M": 1000, "IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}
    n = len(s)
    i = 0
    while i<n:
        if i+1 < n and s[i] + s[i+1] in d:
            ans += d.get(s[i] + s[i+1])
            i += 2
        elif s[i] in d:
            ans += d.get(s[i])
            i += 1
    return ans


def romanToInt(self, s: str) -> int:
    """
    1. Better Approach
    2. Replace IV, IX ..... to plain symbols
    3. Add the particular number to ans
    4. Time Complexity - O(N)
    5. Space Complexity - O(1)
    """
    s = s.replace("IV", "IIII")
    s = s.replace("IX", "VIIII")
    s = s.replace("XL", "XXXX")
    s = s.replace("XC", "LXXXX")
    s = s.replace("CD", "CCCC")
    s = s.replace("CM", "DCCCC")
    ans = 0
    d = {"I": 1, "V":5, "X":10, "L":50, "C":100, "D":500, "M": 1000, "IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}
    for i in s:
        ans += d.get(i)
    return ans