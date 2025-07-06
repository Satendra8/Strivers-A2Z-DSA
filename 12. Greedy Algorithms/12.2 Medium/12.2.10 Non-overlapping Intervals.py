"""
Q. Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Note that intervals which only touch at a point are non-overlapping. For example, [1, 2] and [2, 3] are non-overlapping.

Example 1:

Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.
Example 2:

Input: intervals = [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.
Example 3:

Input: intervals = [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.
"""

def eraseOverlapIntervals(intervals):
    """
    Better Approach
    1. sort the array with last element (to know which one finish faster)
    2. check if prev second <= next first element (check not overlap)
    3. if overlap count it
    Time Complexity: O(NlogN) + O(N)
    Space Complexity: O(N)
    """
    if not intervals:
        return 0
    n = len(intervals)
    intervals.sort(key=lambda x: x[1])
    end = float('-inf')
    i = 0
    overlap = 0

    while i < n:
        if end <= intervals[i][0]:
            end = intervals[i][1]
        else:
            overlap += 1
        i += 1
    return overlap

intervals = [[1,2],[2,3],[3,4],[-100,-2],[5,7]]
print(eraseOverlapIntervals(intervals))



def eraseOverlapIntervals(intervals):
    n = len(intervals)
    intervals.sort(key=lambda x:x[1])
    prev = intervals[0]
    i = 1
    cnt = 0

    while i < n:
        if intervals[i][0] >= prev[1]:
            prev = intervals[i]
        else:
            cnt += 1
        i += 1
    return cnt