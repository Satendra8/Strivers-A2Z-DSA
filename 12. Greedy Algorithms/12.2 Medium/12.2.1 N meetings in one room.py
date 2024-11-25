"""
Q. You are given timings of n meetings in the form of (start[i], end[i]) where start[i] is the start time of meeting i and end[i] is the finish time of meeting i. Return the maximum number of meetings that can be accommodated in a single meeting room, when only one meeting can be held in the meeting room at a particular time. 

Note: The start time of one chosen meeting can't be equal to the end time of the other chosen meeting.

Examples :

Input: start[] = [1, 3, 0, 5, 8, 5], end[] =  [2, 4, 6, 7, 9, 9]
Output: 4
Explanation: Maximum four meetings can be held with given start and end timings. The meetings are - (1, 2), (3, 4), (5,7) and (8,9)

Input: start[] = [10, 12, 20], end[] = [20, 25, 30]
Output: 1
Explanation: Only one meetings can be held with given start and end timings.

Input: start[] = [1, 2], end[] = [100, 99]
Output: 1
"""

def maximumMeetings(start, end):
    """
    Better Approach
    1. Group start and end time
    2. sort by end time
    3. check if next meeting is after end time of previous
    4. initialize last time with -1 to avoid edge case
    Time Complexity: O(NlogN)
    Space Complexity: O(N)
    """
    sorted_list = sorted(list(zip(start,end)), key=lambda x:x[1])
    count = 0
    last_time = -1 # case start=[0], end=[2]

    for elem in sorted_list:
        if elem[0] > last_time:
            count += 1
            last_time = elem[1]
    return count


start = [10, 12, 20]
end = [20, 25, 30]
print(maximumMeetings(start, end))