"""
Q. You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Note that you don't need to modify intervals in-place. You can make a new array and return it.

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
"""

def insert(intervals, newInterval):
    """
    Better Approach
                    |                   |
    intervals = [[1,2],|[3,5],[6,7],[8,10],|[12,16]]
                    |                   |
                Left   |      Mid          | Right

    newInterval = [4,8]

    Left Part
    interval[1] < newInterval[0] # if last element is less then first of new interval
    ans = [[1,2]]

    Middle Part
    interval[0] <= newInterval[1]  #if first element is less then of equal to last of new interval
    pick the smallest and largest among all
    ans = [[1,2], [3,10]]

    Last Part
    Rest elements are Right Part
    ans = [[1,2], [3,10], [12,16]]

    Time Complexity: O(N)
    Space Complexity: O(N)
    """
    n = len(intervals)
    i = 0
    ans = []

    while i < n and intervals[i][1] < newInterval[0]:
        ans.append(intervals[i])
        i += 1
    while i < n and intervals[i][0] <= newInterval[1]:
        newInterval[0] = min(newInterval[0], intervals[i][0])
        newInterval[1] = max(newInterval[1], intervals[i][1])
        i += 1
    ans.append(newInterval)
    while i < n:
        ans.append(intervals[i])
        i += 1            
    return ans

intervals = [[1,3],[6,9]]
newInterval = [2,5]
print(insert(intervals, newInterval))