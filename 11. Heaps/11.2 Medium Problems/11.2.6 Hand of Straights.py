"""
Q. 846. Hand of Straights
Alice has some number of cards and she wants to rearrange the cards into groups so that each group is of size groupSize, and consists of groupSize consecutive cards.

Given an integer array hand where hand[i] is the value written on the ith card and an integer groupSize, return True if she can rearrange the cards, or False otherwise.

Example 1:

Input: hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
Output: True
Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8]
Example 2:

Input: hand = [1,2,3,4,5], groupSize = 4
Output: False
Explanation: Alice's hand can not be rearranged into groups of 4.
"""
import heapq

# Revisit

def isNStraightHand(hand, groupSize):
    """
    1. Use Min heap
    2. use a dict and calculate frequency
    3. pick the smaller element from the heap and find element+1, element+2 .... in dict
    4. if found decrement the frequency count, if not then return false
    5. edge case: top of the heap and element to be deleted will be same, if 1, 1 then 2,2 should present
    Time Complexity: O(nlogn)
    Space Complexity: O(n)
    """
    n = len(hand)

    if n % groupSize == 1:
        return False
    
    d = {}
    for value in hand:
        if value in d:
            d[value] += 1
        else:
            d[value] = 1
    minHeap = [val for val in d.keys()]
    heapq.heapify(minHeap)
    print(minHeap)
    while minHeap:
        top = minHeap[0]
        for i in range(groupSize):
            if top+i in d:
                d[top+i] -= 1

                if d[top+i] == 0:
                    print(top+i, minHeap[0])
                    if top+i != heapq.heappop(minHeap):
                        return False
                    del d[top+i]
            else:
                return False
    return True

def findSuccessors(hand, j, n, groupSize):
    nextElement = hand[j] + 1
    hand[j] = -1
    j += 1
    counter = 1

    while j < n and counter < groupSize:
        if hand[j] == nextElement:
            nextElement = hand[j] + 1
            hand[j] = -1
            counter += 1
        j += 1
    if counter != groupSize:
        return False
    return True


def straightHand(hand, groupSize):
    """
    1. Sort the array
    2. pick 1 element find its all successor and mark -1
    3. if successor not exist return False
    Time Complexity: O(N^2)
    Space Complexity: O(1)
    """
    n = len(hand)
    if n % groupSize == 1:
        return False
    hand.sort()

    for i in range(n):
        if hand[i] == -1:
            continue
        ans = findSuccessors(hand, i, n, groupSize)
        if not ans:
            return False
    return True


hand = [1,1,3,6,2,3,4,7,8]
groupSize = 3
print(straightHand(hand, groupSize))



