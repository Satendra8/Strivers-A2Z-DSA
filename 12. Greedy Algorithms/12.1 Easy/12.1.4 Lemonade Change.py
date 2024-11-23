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

def lemonadeChange(bills):
    """
    1. store count of all coins
    2. if coin is 10 (+10, -5), increase count of 10 by 1 and decrease count of 5 by 1
    3. if coin is 20 (-10, -5) or (-5, -5, -5)
    4. if either 5 or 10 becomes 0 before loop iteration return false
    Time Complexity: O(N)
    Space Complexity: O(N)
    """
    d = {5: 0, 10: 0, 20: 0}
    for coin in bills:
        if coin == 10:
            if d[5] == 0:
                return False
            d[5] -= 1
        elif coin == 20:
            if d[5] == 0:
                return False
            d[5] -= 1

            if d[10] > 0:
                d[10] -= 1
            elif d[5] > 1:
                d[5] -= 2
            else:
                return False
        d[coin] += 1

    return True


bills = [5,10, 20]
print(lemonadeChange(bills))