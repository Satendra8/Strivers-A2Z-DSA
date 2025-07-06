"""
Q. Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
"""

def merge(intervals):
    """
    Better Approach
    1. sort intervals by first element
    2. if intervals not overlap add it to ans (last of prev < first of next)
    3. else merge
    Time Complexity: O(NlogN) + O(N)
    Space Complexity: O(N)
    """
    if not intervals:
        return []
    n = len(intervals)
    intervals.sort(key=lambda x: x[0])
    ans = [intervals[0]]
    i = 1

    while i < n:
        if ans[-1][1] < intervals[i][0]:
            ans.append(intervals[i])
        else:
            ans[-1][1] = max(ans[-1][1], intervals[i][1])
        i += 1
    return ans

intervals = [[1,4],[0,0]]
print(merge(intervals))



def merge(intervals):
    """ similar as prev problem (insert interval)"""
    n = len(intervals)
    intervals.sort(key=lambda x:x[0])
    ans = [intervals[0]]
    i = 1
    print(intervals)
    while i < n and ans[-1][1] < intervals[i][0]:
        ans.append(intervals[i])
        i += 1
    while i < n:
        if ans[-1][1] >= intervals[i][0]:
            ans[-1][0] = min(ans[-1][0], intervals[i][0])
            ans[-1][1] = max(ans[-1][1], intervals[i][1])
        else:
            ans.append(intervals[i])
        i += 1
    return ans


intervals = [[2,3],[2,2],[3,3],[1,3],[5,7],[2,2],[4,6]]
print(merge(intervals))