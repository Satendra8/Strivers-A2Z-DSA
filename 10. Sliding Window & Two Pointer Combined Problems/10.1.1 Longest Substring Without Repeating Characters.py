"""
Q. Given a String, find the length of longest substring without any repeating character.

Example 1:

Input: s = ”abcabcbb”

Output: 3

Explanation: The answer is abc with length of 3.

Example 2:

Input: s = ”bbbbb”

Output: 1

Explanation: The answer is b with length of 1 units.
"""

def lengthOfLongestSubstringBrute(s):
    """
    Brute Force Approach
    1. find all possible substr without duplicate(use set to avoid duplicate)
    2. keep updating the maximum length
    Time Complexity: O(N^2)
    Space Complexity: O(N)
    """
    maxx = 0
    n = len(s)
    for i in range(n):
        st = set()
        for j in range(i, n):
            if s[j] in st:
                maxx = max(maxx, len(st))
                break
            else:
                st.add(s[j])
        maxx = max(maxx, len(st))
    return maxx




def lengthOfLongestSubstringBetter(s):
    """
    Better Approach
    1. take 2 pointers left and right
    2. keep moving right pointers and store in set
    3. if duplicate found remove the prevoius duplicate and values those are prevoius that from stack
    4. keep updating maxx and new value in set
    Time Complexity: O(2N)
    Space Complexity: O(N)
    """
    maxx = 0
    n = len(s)
    left = 0
    st = set()

    for right in range(n):
        if s[right] in st:
            while left < right and s[right] in st:
                st.remove(s[left])
                left += 1
        st.add(s[right])
        maxx = max(maxx, right - left + 1)

    return maxx



def lengthOfLongestSubstringOptimal(s):
    """
    Optimal Approach
    1. Using two pointer with sliding window
    2. using dict to keep letter and its index
    3. if letter is duplicate move the left pointer to 1 ahead of duplicate letter
    4. keep updating maxx and index of duplicate letter in dict
    Time Complexity: O(N)
    Space Complexity: O(N)
    """
    if not s:
        return 0

    n = len(s)
    left = 0
    d = {}
    maxx = 0

    for right in range(n):
        if s[right] in d:
            if d[s[right]] >= left:
                left = d[s[right]] + 1

        maxx = max(maxx, right - left + 1)
        d[s[right]] = right
    return maxx


s = "vavf"
print(lengthOfLongestSubstringOptimal(s))


"""
Optimal Approach Dry Run:
Basic idea: remove the item previous of duplicate element, because that never contribute

    0123456789
s = abcaabcdba

l=6
r=9
maxx=4
dict={a:4, b:8: c:6, d:7} # instead removing the prev element  add condition to ignore if b in dict and dict[b] < l then move l



    0123
s = vavf

l=1
r=3
maxx=3
dict={v:2, a:1, r3 } # instead removing the prev element  add condition to ignore if b in dict and dict[b] < l then move l

"""