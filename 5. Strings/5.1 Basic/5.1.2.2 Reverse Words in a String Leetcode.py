"""
Q. Given an input string s, reverse the order of the words.

Example 1:
Input: s = "the sky is blue"
Output: "blue is sky the"

Example 2:
Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.

Example 3:
Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
"""

def reverse_words(s):
    n = len(s)
    final = ""
    temp = ""
    
    for i in range(n-1, -1, -1):
        if s[i] == " ":
            print(temp)
            if temp and temp != " ":
                if final:
                    final = final + " " + temp
                else:
                    final = temp
            temp = ""
        else:
            temp = s[i] + temp
    if temp and temp != " ":
        final = final + " " + temp
    return final
    
s = "  hello world  "
print(reverse_words(s))