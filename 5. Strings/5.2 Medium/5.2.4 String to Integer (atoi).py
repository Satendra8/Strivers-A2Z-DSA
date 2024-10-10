"""
Q. String to Integer (atoi)
Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).

The algorithm for myAtoi(string s) is as follows:

Read in and ignore any leading whitespace.
Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either. This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
Read in next the characters until the next non-digit character or the end of the input is reached. The rest of the string is ignored.
Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in the range. Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
Return the integer as the final result.

Input: s = "42"
Output: 42
Explanation: The underlined characters are what is read in, the caret is the current reader position.
Step 1: "42" (no characters read because there is no leading whitespace)
         ^
Step 2: "42" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "42" ("42" is read in)
           ^
The parsed integer is 42.
Since 42 is in the range [-231, 231 - 1], the final result is 42.
Example 2:

Input: s = "   -42"
Output: -42
Explanation:
Step 1: "   -42" (leading whitespace is read and ignored)
            ^
Step 2: "   -42" ('-' is read, so the result should be negative)
             ^
Step 3: "   -42" ("42" is read in)
               ^
The parsed integer is -42.
Since -42 is in the range [-231, 231 - 1], the final result is -42.
Example 3:

Input: s = "4193 with words"
Output: 4193
Explanation:
Step 1: "4193 with words" (no characters read because there is no leading whitespace)
         ^
Step 2: "4193 with words" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "4193 with words" ("4193" is read in; reading stops because the next character is a non-digit)
             ^
The parsed integer is 4193.
Since 4193 is in the range [-231, 231 - 1], the final result is 4193.

"""

def myAtoi(self, s: str) -> int:
    """
    1. Brute Force Approach
    2. Trim left white spaces
    3. Check '+' or '-'
    4. Read character untill next digit found
    5. check max and min
    6. Time Complexity - O(N^2)
    6. Space Complexity - O(1)
    """
    ans = "0"
    sign = 1
    MIN, MAX = -2**31, 2**31 - 1
    s = s.lstrip()
    if not s:
        return int(ans)
    l = ['0','1','2','3','4','5','6','7','8','9']
    i = 0
    if s[0] == '-':
        sign = 0
        i += 1
    if s[0] == '+':
        i += 1
    for j in range(i, len(s)):
        if s[j] in l:
            ans += s[j]
        else:
            break
    ans = int(ans)
    if not sign:
        ans = -ans
    if ans > MAX: return MAX
    if ans < MIN: return MIN
    return ans


def myAtoi(self, s: str) -> int:
    """
    1. Better Approach
    2. Trim left white spaces
    3. Check '+' or '-'
    4. Read character untill next digit found
    5. check max and min
    6. Time Complexity - O(N)
    6. Space Complexity - O(1)
    """
    ans = '0'
    MIN, MAX = -2**31, 2**31 -1
    s = s.lstrip()
    i, sign = 0, 1
    if not s:
        return int(ans)
    if s[0] == '-':
        sign = 0
        i += 1
    if s[0] == '+':
        i += 1
    while i < len(s):
        if s[i].isdigit():
            ans += s[i]
        else:
            break
        i += 1
    ans = int(ans)
    if not sign:
        ans = -ans
    if ans > MAX: return MAX
    if ans < MIN: return MIN
    return ans


def myAtoi(s):
    """
    Personal
    """
    #lstrip
    #maintain is_negative
    #skip leading 0
    #check each letter if it is a number and skip i any letter found
    # round if less than 2^-31 then return 2^31, if greater than 2^31 - 1 then 2^31 - 1
    s = s.lstrip()
    MIN, MAX = -2**31, 2**31-1
    is_negative = False
    if s[0] == '-':
        is_negative = True
        s = s[1:]
    elif s[0] == '+':
        s = s[1:]
    s = s.lstrip("0")

    num = 0
    for i in range(len(s)):
        print(s[i], s[i].isnumeric())
        if s[i].isnumeric():
            num = num * 10 + int(s[i])
        else:
            break

    if is_negative:
        num =  -num
    
    if num > MAX: return MAX
    if num < MIN: return MIN
    return num