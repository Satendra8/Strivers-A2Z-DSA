"""
Q. Given a word pat and a text txt. Return the count of the occurrences of anagrams of the word in the text.

Example 1:

Input: txt = "forxxorfxdofr", pat = "for"
Output: 3
Explanation: for, orf and ofr appears in the txt, hence answer is 3.
Example 2:

Input: txt = "aabaabaa", pat = "aaba"
Output: 4
Explanation: aaba is present 4 times in txt.
"""
def matchDict(d1, d2):
    for key in d1.keys():
        if d1[key] != d2.get(key, 0):
            return False
    return True


def search(txt, pat):
    """
    1. Sliding Window
    2. Identification
        i. we are matching substrs
        ii. matching anagrams of  pat
        iii. window size k = len(pat)
    3. store frequency of pattern (using this method, because creation anagram will take O(n!))
    4. form new dict and compare frequency
    5. slide the window, if frequency mathces increment counter
    Time Complexity: O(n)
    Space Complexity: O(26)
    """
    k = len(pat)
    n = len(txt)
    counter = 0
    frequency = {}
    for c in pat:
        if c in frequency:
            frequency[c] += 1
        else:
            frequency[c] = 1
    i = 0
    j = 0
    d = {}

    while j < n:
        if j-i < k:
            if txt[j] in d:
                d[txt[j]] += 1
            else:
                d[txt[j]] = 1
            j += 1
        elif j-i == k:
            if matchDict(frequency, d):
                counter += 1
            d[txt[i]] -= 1
            if d[txt[i]] == 0:
                del d[txt[i]]
            if txt[j] in d:
                d[txt[j]] += 1
            else:
                d[txt[j]] = 1
            i += 1
            j += 1
    if matchDict(frequency, d):
        counter += 1
    return counter

txt = "aabaabaa"
pat = "aaba"

print(search(txt, pat))