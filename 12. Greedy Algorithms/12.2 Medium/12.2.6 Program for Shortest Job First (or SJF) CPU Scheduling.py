"""
Q. Problem Statement: Given a list of job durations representing the time it takes to complete each job. Implement the Shortest Job First algorithm to find the average waiting time for these jobs.

Examples
Example 1:
Input:jobs = [3, 1, 4, 2, 5]
                
Output: 4
Explanation: 
                
The first job that will be executed is of duration 1 and the waiting time for it will be 0.
After the first job, the next shortest job with a duration of 2 will be executed with a waiting time of 1.
Following the completion of the first two jobs, the next shortest job with a duration of 3 will be executed with a waiting time of 3 (1 + 2).
Then, the job with a duration of 4 will be executed with a waiting time of 6 (1 + 2 + 3).
Finally, the job with the longest duration of 5 will be executed with a waiting time of 10 (1 + 2 + 3 + 4).
Hence, the average waiting time is calculated as (0 + 1 + 3 + 6 + 10) / 5 = 20 / 5 = 4.

Example 2:
Input:jobs = [4, 3, 7, 1, 2]
                
Output: 4
Explanation: The first job that will be executed is of duration 1, and the waiting time for it will be 0.
                
After the first job, the next shortest job with a duration of 2 will be executed with a waiting time of 1.
Following the completion of the first two jobs, the next shortest job with a duration of 3 will be executed with a waiting time of 3 (1 + 2).
Then, the job with a duration of 4 will be executed with a waiting time of 6 (1 + 2 + 3).
Finally, the job with the longest duration of 7 will be executed with a waiting time of 10 (1 + 2 + 3 + 4).
Hence, the average waiting time is calculated as (0 + 1 + 3 + 6 + 10) / 5 = 20 / 5 = 4.
"""

def sjf(bt):
    """
    Optimal Approach
    bt = [4,3,7,1,2]
        0 1 2 3 4
    bt = [1,2,3,4,7] #sort

        1     2       3       4       7
    0------1------3-------6-------10-------17

    process  waiting time
    p0 -------> 0
    p1 -------> 1
    p2 -------> 3
    p3 -------> 6
    p4 -------> 10
    -------------------
    total       20
    -------------------
    AVG = 20/5 = 4

    Time Complexity: O(N)
    Space Complexity: O(1)
    """
    n = len(bt)
    bt.sort()
    waiting_time = 0
    total_time = 0

    for i in range(n-1):
        waiting_time += bt[i]
        total_time += waiting_time
    return int(total_time/n)


bt = [1,2,3,4]
print(sjf(bt))