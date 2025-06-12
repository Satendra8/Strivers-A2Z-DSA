"""
Q. You will be given a string and an integer k, Your task is to figure out the longest substring which has atmost k distinct characters.

Example 1: s = 'aaabbccd', k = 2 

"""

def longestSubStr(s, k):
    """
    Brute Force Approach
    1. Generate all possible subarrays
    2. keep adding in set
    3. if length of set exceeds k update the max length and break
    Time Complexity: O(N^2)
    Space Complexity: O(256)
    """
    n = len(s)
    ans = 0

    for i in range(n):
        st = set()
        for j in range(i ,n):
            st.add(s[j])

            if len(st) > k:
                ans = max(ans, j - i)
                break
    return ans



def longestSubStrBetter(s, k):
    """
    Better Approach
    1. Use two pointer with sliding window
    2. keep moving the right pointer and updating the ans
    3. if length of set exceeds k keep removing from left untill lenght <= k
    Time Complexity: O(2N)
    Space Complexity: O(256)
    """
    n = len(s)
    left = 0
    d = {}
    ans = 0

    for right in range(n):
        if s[right] in d:
            d[s[right]] += 1
        else:
            d[s[right]] = 1
    
        while len(d) > k:
            d[s[left]] -= 1
            left += 1
            if d[s[left]] == 0:
                d.pop(d[s[left]])
        
        ans = max(ans, right - left + 1)
    return ans



def longestSubStrOptimal(s, k):
    """
    Optimal Approach
    1. Use two pointer with sliding window
    2. keep moving the right pointer and updating the ans
    3. if length of set exceeds k remove 1 element from left (keep the window as maximum)
    4. update the max only of k not exceeds
    Time Complexity: O(N)
    Space Complexity: O(256)
    """
    n = len(s)
    left = 0
    d = {}
    ans = 0

    for right in range(n):
        if s[right] in d:
            d[s[right]] += 1
        else:
            d[s[right]] = 1
    
        if len(d) > k:
            d[s[left]] -= 1
            left += 1
            if d[s[left]] == 0:
                d.pop(d[s[left]])
        if len(d) <= k:
            ans = max(ans, right - left + 1)
    return ans

s = 'aaabbccd'
k = 2
print(longestSubStrOptimal(s, k))