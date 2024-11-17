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