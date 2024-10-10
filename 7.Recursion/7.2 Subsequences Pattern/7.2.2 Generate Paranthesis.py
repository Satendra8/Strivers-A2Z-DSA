"""
Q. Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]

"""


def generateParenthesis(opening, closing, ans, finalList):
    """
    1. base case: if opening and closing are 0 (ans is present at leaf node)
    2. make choice for '('
    3. make choice for ')', if opening < closing (means there should be a opened bracket)
    """

    if opening == 0 and closing == 0:
        finalList.append(ans)
        return
    
    if opening > 0:
        generateParenthesis(opening-1, closing, ans + '(', finalList)
    if closing > 0 and opening < closing:
        generateParenthesis(opening, closing-1, ans + ')', finalList)
    return

n = 1
finalList = []
generateParenthesis(n, n, "", finalList)
print(finalList)
