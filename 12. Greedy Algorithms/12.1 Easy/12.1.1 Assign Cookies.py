"""
Q. Assume you are an awesome parent and want to give your children some cookies. But, you should give each child at most one cookie.

Each child i has a greed factor g[i], which is the minimum size of a cookie that the child will be content with; and each cookie j has a size s[j]. If s[j] >= g[i], we can assign the cookie j to the child i, and the child i will be content. Your goal is to maximize the number of your content children and output the maximum number.


Example 1:

Input: g = [1,2,3], s = [1,1]
Output: 1
Explanation: You have 3 children and 2 cookies. The greed factors of 3 children are 1, 2, 3. 
And even though you have 2 cookies, since their size is both 1, you could only make the child whose greed factor is 1 content.
You need to output 1.


Example 2:

Input: g = [1,2], s = [1,2,3]
Output: 2
Explanation: You have 2 children and 3 cookies. The greed factors of 2 children are 1, 2. 
You have 3 cookies and their sizes are big enough to gratify all of the children, 
You need to output 2.
"""

def findContentChildren(g, s):
    """
    Brute Force Approach
    1. sort the childrens which has low greed will come first
    2. assing cookie for all using 2 nested loops
    Time Complexity: O(N^2)
    Space Complexity: O(1)
    """
    s.sort()
    print(s)
    n = len(s)
    count = 0

    for i in g:
        for j in range(n):
            if s[j] >= j:
                s[j] = -1
                count += 1
                break
    return count



def findContentChildrenOptimal(g, s):
    """
    Optimal Approach
    1. sort both array
    2. use to pointers and check for less than or equal to element
    3. if matches increase both pointers else increase only one pointer
    Time Complexity: O(NlongN + MlogM + N)
    Space Complexity: O(1)
    
    """
    n = len(s)
    s.sort()
    g.sort()
    l = 0
    r = 0

    while r < n and l < len(g):
        if s[r] >= g[l]:
            r += 1
            l += 1
        else:
            r += 1
    return l

g = [1,2,3]
s = [1,1]
print(findContentChildrenOptimal(g, s))

"""

g = [1,5,3,3,4]
s = [4,2,1,2,1,3]

s = [-1,1,2,2,-1,4]

count = 3

"""