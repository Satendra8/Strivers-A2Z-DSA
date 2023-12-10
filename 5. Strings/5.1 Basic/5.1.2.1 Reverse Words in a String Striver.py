"""
Q. Given a string s, reverse the words of the string.

Example 1:
Input: s="this is an amazing program"
Output: "program amazing an is this"

Example 2:
Input: s="This is decent"
Output: "decent is This"

"""

def reverse_words(s):
    """
1. Brute Force Approach
2. Time Complexity - O(N)
3. Space Complecity - O(N)
    """
    
    l = s.split()
    l.reverse()
    s = " ".join(l)
    return s

s = "this is an amazing program"
print(reverse_words(s))



def reverse_words(s):
    """
1. Optimized Approach
2. Not using list
3. Apeend word in reverse order till space comes
4. Time Complexity - O(N)
5. Space Complexity - O(1) //space is used to return the outputs
    """
    final_ans = ""
    temp_str = ""
    for i in range(len(s)-1, -1, -1):
        if s[i] == " ":
            if not final_ans:
                final_ans = temp_str
            else:
                final_ans  = final_ans + " " + temp_str
            temp_str = ""
        else:
            temp_str = s[i]+temp_str
    if temp_str:
        final_ans = final_ans + " " + temp_str
    return final_ans
    
s = "this is an amazing program"    
print(reverse_words(s))