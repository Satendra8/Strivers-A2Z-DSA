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