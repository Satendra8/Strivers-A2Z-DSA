"""
Q. There are several cards arranged in a row, and each card has an associated number of points. The points are given in the integer array cardPoints.

In one step, you can take one card from the beginning or from the end of the row. You have to take exactly k cards.

Your score is the sum of the points of the cards you have taken.

Given the integer array cardPoints and the integer k, return the maximum score you can obtain.


Example 1:

Input: cardPoints = [1,2,3,4,5,6,1], k = 3
Output: 12
Explanation: After the first step, your score will always be 1. However, choosing the rightmost card first will maximize your total score. The optimal strategy is to take the three cards on the right, giving a final score of 1 + 6 + 5 = 12.

Example 2:

Input: cardPoints = [2,2,2], k = 2
Output: 4
Explanation: Regardless of which two cards you take, your score will always be 4.

Example 3:

Input: cardPoints = [9,7,7,9,7,7,9], k = 7
Output: 55
Explanation: You have to take all the cards. Your score is the sum of points of all cards.
"""

def maxScore(cardPoints, k):
    """
    Optimal Approach
    1. find sum of first k elements from left
    2. keep removing kth, kth-1, kth-2 ....0 and taking from right
    3. keep updating the maximum as ans
    Time Complexity: O(2k)
    Space Complexity: O(1)
    """
    n = len(cardPoints)
    left = k-1
    right = n-1
    ans = 0

    summ = sum(cardPoints[:k])
    ans = max(summ, ans)

    while left >= 0:
        summ -= cardPoints[left]
        summ += cardPoints[right]
        left -= 1
        right -= 1
        ans = max(ans, summ)
    return ans

cardPoints = [6,2,3,4,7,2,1,7,1]
k = 4
print(maxScore(cardPoints, k))

"""
cardPoints = [9,7,7,9,7,7,9]
k = 7

"""


def maximum(cardPoints, k):
    """
    Sliding window
    take first k elements
    keep removing 1 by 1 and take from last
    keep updating max
    """
    n = len(cardPoints)
    i = k-1
    j = n-1
    lsum = sum(cardPoints[:k])
    rsum = 0
    ans = lsum + rsum

    while i >= 0:
        lsum -= cardPoints[i]
        rsum += cardPoints[j]
        ans = max(ans, lsum+rsum)
        i -= 1
        j -= 1
    return ans
        

cardPoints = [1,2,3,4,5,6,1]
k = 3
print(maximum(cardPoints, k))

"""
cardPoints = [11,49,100,20,86,29,72]
k = 4

lsum = 180  rsum = 0  ans = 0
lsum = 160  rsum = 72  ans = 232
lsum = 60  rsum = 101  ans = 161
lsum = 11  rsum = 187  ans = 197
lsum = 0  rsum = 207  ans = 207

i = 0
j = 3

"""