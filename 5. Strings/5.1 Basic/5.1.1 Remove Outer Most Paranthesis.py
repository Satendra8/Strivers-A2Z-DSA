"""
Q. Remove Outermost Parentheses

Example 1:

Input: s = "(()())(())"
Output: "()()()"
Explanation: 
The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
After removing outer parentheses of each part, this is "()()" + "()" = "()()()".

Example 2:

Input: s = "(()())(())(()(()))"
Output: "()()()()(())"
Explanation: 
The input string is "(()())(())(()(()))", with primitive decomposition "(()())" + "(())" + "(()(()))".
After removing outer parentheses of each part, this is "()()" + "()" + "()(())" = "()()()()(())".

Example 3:

Input: s = "()()"
Output: ""
Explanation: 
The input string is "()()", with primitive decomposition "()" + "()".
After removing outer parentheses of each part, this is "" + "" = "".

Constraints:

1 <= s.length <= 105
s[i] is either '(' or ')'.
s is a valid parentheses string.

"""

def remove_outer_paranthesis(s):
    """
    1. Brute Force Approach
    2. Iterate over all characters
    3. push into temp list (using it as stack)
    4. if '(' comes up check if lenght of stack is greater than 1 because we don't count outer bracket then then it to ans
    5. if ')' comes up check the length of stack if more than 1 then add it to answer and pop last element '(' from stack
    6. Time Complexity - O(N)
    7. Space Complexity - O(N)
    """
    ans = ""
    temp = []
    
    for i in s:
        if i == '(':
            temp.append('(')
            if(len(temp) > 1):
                ans += '('
            
        if i == ')':
            if len(temp)>1:
                ans += ')'
            temp.pop()
    return ans
    
s = "()()"
print(remove_outer_paranthesis(s))



def remove_outer_paranthesis(s):
    """
    1. Optimized Approach
    2. Iterate over all characters
    3. for '(' increment the counter if '(' is not first open bracket then append it to ans
    4. for ')' decrement the counter if ')' is not last closed bracket then append it to ans
    5. Time Complexity - O(N)
    6. Space Complexity - O(1)
    """    
    ans = ""
    opened = 0
    
    for i in s:
        if i == '(':
            opened += 1
            if opened > 1:
                ans += '('
        elif i == ')':
            opened -= 1
            if opened > 0:
                ans += ')'
    return ans

s = '(()())(())(()(()))'
print(remove_outer_paranthesis(s))