"""
Q. Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.

The following rules define a valid string:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".
 

Example 1:

Input: s = "()"
Output: true

Example 2:

Input: s = "(*)"
Output: true

Example 3:

Input: s = "(*))"
Output: true
"""

def checkParanthesis(s):
    count = 0

    for i in range(len(s)):
        if s[i] == '(':
            count += 1
        elif s[i] == ')':
            count -= 1
        if count < 0:
            return False
    if count == 0:
        return True
    return False

def checkValidStringBasic(s, ind, n, ans):
    i = ind
    for i in range(ind, n):
        if s[i] == '*':
            if checkValidStringBasic(s, i+1, n, ans+'('):
                return True
            if checkValidStringBasic(s, i+1, n, ans+')'):
                return True
        
            if checkValidStringBasic(s, i+1, n, ans+''):
                return True
            break
        else:
            ans += s[i]
    if i == n-1:
        return checkParanthesis(ans)
    return False




def checkValidStringBrute(s, ind, count, n):
    """
    Brute Force Approach
    Generate all possible solutions using recursion
    1. keep a counter to store balance parenthesis
    2. if ( increment, if ) decrement
    3. if * then call recursion on with ( do +1, ) do -1, '' do nothing
    4. base case, if count becomes -ve or length exceeds
    5. Time Complexity: 3^N
    6. Space Complexity: N (depth of recursion)
    """
    if count < 0:
        return False
    if ind == n:
        if count == 0:
            return True
        return False

    if s[ind] == '*':
        if checkValidStringBrute(s, ind+1, count+1, n):
            return True
        if checkValidStringBrute(s, ind+1, count-1, n):
            return True
        if checkValidStringBrute(s, ind+1, count, n):
            return True
    else:
        if s[ind] == '(':
            count += 1
        else:
            count -= 1
        return checkValidStringBrute(s, ind+1, count, n)
    return False


def checkValidStringBetter(s):
    """
    Better Approach
    1. use 2 stacks left and star
    2. keep pushing left and star
    3. if ) pop either from left or star
    4. now pop ( if there is remaing with star
    5. edge case: ( should be always left to star
    Time Complexity: O(N)
    Space Complexity: O(N) 
    """
    n = len(s)

    left = []
    star = []

    for i in range(n):
        if s[i] == '(':
            left.append(i)
        elif s[i] == ')':
            if left:
                left.pop()
            elif star:
                star.pop()
            else:
                return False
        else:
            star.append(i)

    while left and star:
        if left[-1] > star[-1]:  # Ensure unmatched '(' comes before available '*'
            return False
        left.pop()
        star.pop()
    if left:
        return False
    return True



def checkValidStringOptimal(s):
    """
    Use Greedy Approach
    1. use two variable to keep minimum and maximum left paranthesis
    2. if ( increment both
    3. if ) decrement both
    4. if * once consider ) (decrement min) once ( (increment max)
    5. if max becomes negative return false
    6. if min becomes 0 than return true
    Time Complexity: O(N)
    Space Complexity: O(N)
    """
    minLeft = 0
    maxLeft = 0

    for c in s:
        if c == '(':
            minLeft += 1
            maxLeft += 1
        elif c == ')':
            minLeft -= 1
            maxLeft -= 1
        else:
            minLeft -= 1 #considering it to be )
            maxLeft += 1 #considering it to be (
        
        if maxLeft < 0:
            return False
        if minLeft < 0:
            minLeft = 0

    return minLeft == 0

s = '(*))'
print(checkValidStringBetter(s))