"""
Q. Given an array, jobs[] where each job[i] has a jobid, deadline and profit associated with it. Each job takes 1 unit of time to complete and only one job can be scheduled at a time. We earn the profit associated with a job if and only if the job is completed by its deadline.

Find the number of jobs done and the maximum profit.

Note: jobs will be given in the form (jobid, deadline, profit) associated with that job. Deadline of the job is the time on or before which job needs to be completed to earn the profit.

Examples :

Input: jobs[] = [(1,4,20), (2,1,1), (3,1,40), (4,1,30)]
Output: [2, 60]
Explanation: job1 and job3 can be done with maximum profit of 60 (20+40).

Input: jobs[] = [(1,2,100), (2,1,19), (3,2,27), (4,1,25), (5,1,15)]
Output: [2, 127]
Explanation: 2 jobs can be done with maximum profit of 127 (100+27).

Input: jobs[] = [(1,3,50), (2,1,10), (3,2,20), (4,2,30)]
Output: [2, 80]
Explanation: Job 1 and Job 4 can be completed with a maximum profit of 80 (50 + 30).
"""

def minimumPlatform(arr, dep):
    """
    Brute Force Approach
    1. use nested loop and find maximum number of intersection
    2. check if arrival time of i lies between j
    3. or if arrival time of j lies between i
    4. keep updating the maximum count
    Time Complexity: O(N^2)
    Space Complexity: O(1)
    """
    n = len(arr)
    maxIntersect = 1

    for i in range(n):
        intersect = 1
        for j in range(i+1, n):
            if arr[i] <= arr[j] <= dep[i] or arr[j] <= arr[i] <= dep[j]:
                intersect += 1
        maxIntersect = max(maxIntersect, intersect)
    return maxIntersect


def minimumPlateformOptimal(arr, dep):
    """
    Optimal Approach
    1. arr[] = [1000, 935, 1100], dep[] = [1200, 1240, 1130]
    2. combine and sort arr and dep [(935, A), (1000, A), (1100, A), (1130, D), (1200, D), (1240, D)]
    3. for arrival count + 1, for dep -1
    4. keep the maximum count that will be the ans
    Time Complexity: O(NlogN)
    Space Complexity: O(N)    
    """
    
    n = len(arr)
    max_cnt = 0
    cnt = 0
    i=0
    j=0
    arr.sort()
    dep.sort()

    while i < n and j < n:
        if arr[i] < dep[j]:
            cnt += 1
            i += 1
        else:
            cnt -= 1
            j += 1
        max_cnt = max(max_cnt, cnt)

    max_cnt = max(max_cnt, cnt)
    return max_cnt

    
        

arr = [1114, 825, 357, 1415, 54]
dep = [1740, 1110, 2238, 1535, 2323]
print(minimumPlateformOptimal(arr, dep))


arr = [1114, 825, 357, 1415, 54]
dep = [1740, 1110, 2238, 1535, 2323]
#output 4