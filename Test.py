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