"""
Q. You are visiting a farm that has a single row of fruit trees fruitsanged from left to right. The trees are represented by an integer fruitsay fruits where fruits[i] is the type of fruit the ith tree produces.

You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
Given the integer fruitsay fruits, return the maximum number of fruits you can pick.

Example 1:

Input: fruits = [1,2,1]
Output: 3
Explanation: We can pick from all 3 trees.
Example 2:

Input: fruits = [0,1,2,2]
Output: 3
Explanation: We can pick from trees [1,2,2].
If we had started at the first tree, we would only pick from trees [0,1].
Example 3:

Input: fruits = [1,2,3,2,2]
Output: 4
Explanation: We can pick from trees [2,3,2,2].
If we had started at the first tree, we would only pick from trees [1,2].
"""


def totalFruit(fruits):
    """
    1. Sliding Window variable
    2. similar to longest substring with 2 unique characters
    Time Complexity: O(N)
    Space Complexity: O(1)
    """
    N = len(fruits)
    i = 0
    j = 0
    d = {}
    ans = 0
    K = 2

    while j < N:
        if fruits[j] in d:
            d[fruits[j]] += 1
        else:
            d[fruits[j]] = 1
        
        print(d, j)
        if len(d) == K:
            ans = max(ans, j-i+1)
        elif len(d) > K:
            while len(d) > K:
                d[fruits[i]] -= 1
                if d[fruits[i]] == 0:
                    del d[fruits[i]]
                i += 1
                if len(d) == K:
                    ans = max(ans, j-i+1)
        else:
            ans = max(ans, j-i+1)
        j += 1
    return ans


fruits = [0]
print(totalFruit(fruits))

"""
fruits = [0,1,2]
j = 2
i = 0
d = {0:1, 1:1}
ans = 0
"""