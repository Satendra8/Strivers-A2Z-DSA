"""
Q. Remove Outermost Parentheses

Example 1:

Input Format: s = "(()())(())"
Result: "()()()"
Explanation: 
The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
After removing outer parentheses of each part, this is "()()" + "()" = "()()()".

Example 2:

Input Format: s = "(()())(())(()(()))"
Result: "()()()()(())"
Explanation: 
The input string is "(()())(())(()(()))", with primitive decomposition "(()())" + "(())" + "(()(()))".
After removing outer parentheses of each part, this is "()()" + "()" + "()(())" = "()()()()(())".

Example 3:

Input Format: s = "()()"
Result: ""
Explanation: 
The input string is "()()", with primitive decomposition "()" + "()".
After removing outer parentheses of each part, this is "" + "" = "".

Constraints:

1 <= s.length <= 105
s[i] is either '(' or ')'.
s is a valid parentheses string.

"""

def remove_outer_paranthesis(string):
    """
    1. Brute Force Approach
    2. Iterate over all characters
    3. push into temp list (using it as stack)
    4. if '(' comes up check if lenght of stack is greater than 1 because we don't count outer bracket then add it to ans
    5. if ')' comes up check the length of stack if more than 1 then add it to answer and pop last element '(' from stack
    6. Time Complexity - O(N)
    7. Space Complexity - O(N)
    """
    ans = ""
    temp = []
    
    for letter in string:
        if letter == '(':
            temp.append('(')
            if(len(temp) > 1):
                ans += '('
            
        if letter == ')':
            if len(temp)>1:
                ans += ')'
            temp.pop()
    return ans
    
if __name__ == '__main__':
    string = "(()())(())(()(()))"
    print(remove_outer_paranthesis(string))



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
    
    for letter in string:
        if letter == '(':
            opened += 1
            if opened > 1:
                ans += '('
        elif letter == ')':
            opened -= 1
            if opened > 0:
                ans += ')'
    return ans

string = '(()())(())(()(()))'
print(remove_outer_paranthesis(string))
