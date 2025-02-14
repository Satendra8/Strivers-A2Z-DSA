"""
Q. We can scramble a string s to get a string t using the following algorithm:

If the length of the string is 1, stop.
If the length of the string is > 1, do the following:
Split the string into two non-empty substrings at a random index, i.e., if the string is s, divide it to x and y where s = x + y.
Randomly decide to swap the two substrings or to keep them in the same order. i.e., after this step, s may become s = x + y or s = y + x.
Apply step 1 recursively on each of the two substrings x and y.
Given two strings s1 and s2 of the same length, return true if s2 is a scrambled string of s1, otherwise, return false.

Example 1:

Input: s1 = "great", s2 = "rgeat"
Output: true
Explanation: One possible scenario applied on s1 is:
"great" --> "gr/eat" // divide at random index.
"gr/eat" --> "gr/eat" // random decision is not to swap the two substrings and keep them in order.
"gr/eat" --> "g/r / e/at" // apply the same algorithm recursively on both substrings. divide at random index each of them.
"g/r / e/at" --> "r/g / e/at" // random decision was to swap the first substring and to keep the second substring in the same order.
"r/g / e/at" --> "r/g / e/ a/t" // again apply the algorithm recursively, divide "at" to "a/t".
"r/g / e/ a/t" --> "r/g / e/ a/t" // random decision is to keep both substrings in the same order.
The algorithm stops now, and the result string is "rgeat" which is s2.
As one possible scenario led s1 to be scrambled to s2, we return true.
Example 2:

Input: s1 = "abcde", s2 = "caebd"
Output: false
Example 3:

Input: s1 = "a", s2 = "a"
Output: true
"""

def solve(s1, s2):
    """
    Variation of MCM
    1. split the problem into 2 parts
                      |          |
        i. swapped: gr|eat    ate|gr     (check left part of first str and right part of second str) (gr, gr)
                      |          |       (check right part of first str and left part of second str) (eat, ate)

                           |          |
        ii. not swapped: gr|eat     gr|eat     (check left part of both) (gr, gr)
                           |          |        (check right part both) (eat, eat)
    2. base condition 1:  if len of s1 and s2 differnt, then scrimble not possible
    3. base condition 2: if both are empty then consider as scrimble
    4. if both string match then True
    5. if single len string remaining but not match return False
    6. k loop: 1 to n-1, so this string is splitable without ''
    7. at any moment True found, return True
    """
    if s1 == s2:
        return True

    # no furthur splitable
    if len(s1) <= 1 or len(s2) <= 1:
        return False

    n = len(s1)
    for k in range(1, n):
        if (solve(s1[0:k], s2[n-k:n]) and solve(s1[k:n], s2[0:n-k])) or (solve(s1[0:k], s2[0:k]) and solve(s1[k:n], s2[k:n])):
            return True
    return False


def isScramble(s1, s2):
    if len(s1) != len(s2):
        return False
    
    if not s1 or not s2:
        return True

    return solve(s1, s2)



def solveMemoization(s1, s2, mp):
    """
    Variation of MCM
    1. split the problem into 2 parts
                      |          |
        i. swapped: gr|eat    ate|gr     (check left part of first str and right part of second str) (gr, gr)
                      |          |       (check right part of first str and left part of second str) (eat, ate)

                           |          |
        ii. not swapped: gr|eat     gr|eat     (check left part of both) (gr, gr)
                           |          |        (check right part both) (eat, eat)
    2. base condition 1:  if len of s1 and s2 differnt, then scrimble not possible
    3. base condition 2: if both are empty then consider as scrimble
    4. if both string match then True
    5. if single len string remaining but not match return False
    6. k loop: 1 to n-1, so this string is splitable without ''
    7. at any moment True found, return True
    """
    if s1 == s2:
        return True

    # no furthur splitable
    if len(s1) <= 1 or len(s2) <= 1:
        return False
    
    key = f"{s1}_{s2}"
    if key in mp:
        return mp[key]

    n = len(s1)
    for k in range(1, n):
        if (solveMemoization(s1[0:k], s2[n-k:n], mp) and solveMemoization(s1[k:n], s2[0:n-k]), mp) or (solveMemoization(s1[0:k], s2[0:k], mp) and solveMemoization(s1[k:n], s2[k:n], mp)):
            mp[key] = True
            return True
    mp[key] = False
    return False


def isScrambleMomoizarion(s1, s2):
    if len(s1) != len(s2):
        return False
    
    if not s1 or not s2:
        return True

    mp = dict()
    return solveMemoization(s1, s2, mp)

s1 = "a"
s2 = "a"
print(isScrambleMomoizarion(s1, s2))