"""
Q. Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.
Return the sorted string. If there are multiple answers, return any of them.

Example 1:
Input: s = "tree"
Output: "eert"
Explanation: 'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

Example 2:
Input: s = "cccaaa"
Output: "aaaccc"
Explanation: Both 'c' and 'a' appear three times, so both "cccaaa" and "aaaccc" are valid answers.
Note that "cacaca" is incorrect, as the same characters must be together.

Example 3:
Input: s = "Aabb"
Output: "bbAa"
Explanation: "bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.
"""

def frequency_sort(s):
    """
    1. Better Approach
    2. Count frequency of all elements
    3. Sort dict by value in reverse order
    4. loop over all dict items and print
    5. Time Complexity - O(NlogN)
    6. Space Complexity - O(N)
    """
    n = len(s)
    ans = ""
    d = {}
    for i in s:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    d = sorted(d.items(), key = lambda x:x[1], reverse=True)
    for key, value in d:
        ans += key * value
    return ans


s = "Aabb"
print(frequency_sort(s))