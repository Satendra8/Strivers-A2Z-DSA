"""
Q. Given two strings, check if two strings are anagrams of each other or not.

Example 1:
Input: CAT, ACT
Output: true
Explanation: Since the count of every letter of both strings are equal.

Example 2:
Input: RULES, LESRT 
Output: false
Explanation: Since the count of U and T  is not equal in both strings.
"""


def anagram(s, k):
    """
    1. Brute Force Approach
    2. match the lenght
    3. Iterate and match the count of i in both str
    4. Time Complexity - O(N^2)
    5. Space Compleity - O(1)

    """
    if len(s) != len(k):
        return False
        
    for i in s:
        if s.count(i) != k.count(i):
            return False
    return True
    
s = "CATC"
k = "ACTC"
print(anagram(s, k))


def anagram(s, k):
    """
    1. Better Approach
    2. check if lenght is equal
    3. sort the string and match
    4. Time Complexity - O(NlogN)
    5. Space Complexity - O(1) //using same variable
    
    """
    if len(s) != len(k):
        return False
    s = ''.join(sorted(s))
    k = ''.join(sorted(k))
    if s != k:
        return False
    return True
    
s = "CATA"
k = "ACTC"
print(anagram(s, k))
import json

def anagram(s, k):
    """
    1. Optimized Approach
    2. Compare length
    3. Store character count in an array (A-Z) for s
    4. Iterate over k and subtract the count
    5. If temp_arr has all element 0, then it is anagram
    6. Time Complexity - O(N)
    7. Space Complexity - O(1) 
    """
    if len(s) != len(k):
        return False
    temp_arr = [0]*26
    
    for i in s:
        temp_arr[ord(i) - 65] += 1
    for j in k:
        temp_arr[ord(j) - 65] -= 1
    for i in temp_arr:
        if i != 0:
            return False
    
    return True

s = "INTEGER"
k = "NTEGERI"
print(anagram(s, k))


def anagrams(s, k):
    """
    Personal Approach
    """

    if len(s) != len(k):
        return False
    
    d = {}

    for i in range(len(s)):
        if s[i] in d:
            d[s[i]] += 1
        else:
            d[s[i]] = 1
    print(d)

    for i in range(len(k)):
        if k[i] in d:
            d[k[i]] -= 1
        else:
            d[k[i]] = 1
    print(d)
    for key, value in d.items():
        if value != 0:
            return False
    return True