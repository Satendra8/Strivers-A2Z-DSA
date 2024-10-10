"""
Q. Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""

def longest_common_prefix(strs):
    """
    1. Brute Force Approach
    2. used 2 nested loops, 1 for tracking current character
    3. another one for iterating over all array elements
    4. check if current element character not matched with current character then return
    5. added an extra check because lenght of all elements are not equal
    6. Time Complexity - O(N^2)
    7. Space Complexity - O(L): L is length of Output string
    """
    n = len(strs[0])
    common = ""
    for i in range(n):
        curr = strs[0][i]
        for element in strs:
            if len(element) < i+1 or element[i] != curr:
                return common
        common += curr
                
    return common
    
strs = ["flower", "flowweerr", "flowwwwwww"]
print(longest_common_prefix(strs))


def longest_common_prefix(strs):
    """
    1. Optimal Approach
    2. As we need to find common characters in all elements, just check the first and last element
    3. need to sort so that not/less similar element will come at last
    4. Iterate and match each character of first and last element
    5. Time Complexity - O(N*Log(N))
    6. Space Complexity - O(L): L is length of Output string
    """
    strs.sort()
    print(strs)
    common = ""
    first = strs[0]
    last = strs[-1]
    n = min(len(first), len(last))
    
    for i in range(n):
        if first[i] != last[i]:
            return common
        common += first[i]
    return common
    
strs = ["aaa","aa","aaa"]
print(longest_common_prefix(strs))