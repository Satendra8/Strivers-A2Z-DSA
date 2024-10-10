"""
Q. Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Example 1:

Input: num = 3
Output: "III"
Explanation: 3 is represented as 3 ones.
Example 2:

Input: num = 58
Output: "LVIII"
Explanation: L = 50, V = 5, III = 3.
Example 3:

Input: num = 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.   
"""


def intToRoman(self, num: int) -> str:
    """
    1. Brute Force Approach
    2. Subrate the highest number from input numer till it becomes 0
    3. Starting from the largest number
    4. Time Complexity - O(N)
    4. Space Complexity - O(1)
    """

    d = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
    l = [1000, 500, 100, 50, 10, 5, 1]
    ans = ""
    while num > 0:
        print(num)
        for i in l:
            if i <= num:
                ans += d[i]
                num -= i
                break
        print(ans)
    
    ans = ans.replace('DCCCC', 'CM')
    ans = ans.replace('CCCC', 'CD')
    ans = ans.replace('LXXXX', 'XC')
    ans = ans.replace('XXXX', 'XL')
    ans = ans.replace('VIIII', 'IX')
    ans = ans.replace('IIII', 'IV')
    return ans



def intToRoman(self, num: int) -> str:
    """
    1. Better Approach
    2. Make A dict of all Symbols and their number
    3. 3214//1000 = 3*M  = MMM (using this approach)
    4. Time Complexity - O(1)
    4. Space Complexity - O(1)
    """

    d = {1000 : "M",
    900 : "CM",
    500 : "D",
    400 : "CD",
    100 : "C",
    90 : "XC",
    50 : "L",
    40 : "XL",
    10 : "X",
    9 : "IX",
    5 : "V",
    4 : "IV",
    1 : "I"}
    ans = ""
    for key, value in d.items():
        if num <= 0:
            break
        ans += (num//key)*value
        num  = num%key
        print(num)
    return ans



def intToRoman(num):
    """
    Personal
    """
    d = {
        1000: "M",
        500: "D",
        100: "C",
        50: "L",
        10: "X",
        5: "V",
        1: "I",
        4: "IV",
        9: "IX",
        40: "XL",
        90: "XC",
        400: "CD",
        900: "CM",

    }
    l = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    ans = ""

    for i in l:
        while num >= i:
            num -= i
            ans += d[i]
    return ans