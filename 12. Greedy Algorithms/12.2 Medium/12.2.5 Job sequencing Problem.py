"""
Q. Problem Statement: You are given a set of N jobs where each job comes with a deadline and profit. The profit can only be earned upon completing the job within its deadline. Find the number of jobs done and the maximum profit that can be obtained. Each job takes a single unit of time and only one job can be performed at a time.

Examples

Example 1:

Input: N = 4, Jobs = {(1,4,20),(2,1,10),(3,1,40),(4,1,30)}

Output: 2 60

Explanation: The 3rd job with a deadline 1 is performed during the first unit of time .The 1st job is performed during the second unit of time as its deadline is 4.
Profit = 40 + 20 = 60

Example 2:

Input: N = 5, Jobs = {(1,2,100),(2,1,19),(3,2,27),(4,1,25),(5,1,15)}

Output: 2 127

Explanation: The  first and third job both having a deadline 2 give the highest profit. 
Profit = 100 + 27 = 127
"""

class Job:    
    def __init__(self,id, deadline=0, profit=0):
        self.id = id
        self.deadline = deadline
        self.profit = profit

class Solution:
    def jobScheduling(Jobs):
        """
        Better Approach
        1. sort jobs by profit desc
        2. take an array as slot to the maximum deadline
        3. pick the job and assign to its maximum slot if available
        4. keep updating the profit and job count
        Time Complexity: O(NlogN) + max_deadline + O(N*max_deadline)
        Space Complexity: O(max_deadline)
        """
        profit = 0
        count = 0
        Jobs = sorted(Jobs, key=lambda x: x.profit, reverse=True)
        maxi = max(job.deadline for job in Jobs)
        arr = [-1]*(maxi+1)

        for job in Jobs:
            for i in range(job.deadline, 0, -1):
                if arr[i] == -1:
                    arr[i] = job.id
                    profit += job.profit
                    count += 1
                    break
        return [count, profit]

jobs = [Job(1,3,50), Job(2,1,10), Job(3,2,20), Job(4,2,30)]
print(Solution.jobScheduling(jobs))


def jobSequencing(profits, deadlines):
    """
    1. sort by profit desc
    2. create slot of max(deadlines)
    3.  0___1___2___3___4
    4. put the max profit job by their deadline, if there is aleady an element on deadline then move backward to check empty slots
    Time Complexity: NlogN + N * slots
    Space Complexity: N + slots
    """
    slots = max(deadlines)
    jobs = zip(profits, deadlines)
    jobs = sorted(jobs, key=lambda x: x[0], reverse=True)
    slot_array = [0]*slots
    count = 0

    for p, d in jobs:
        # for optimization use Disjoint Unioun Set to replace the below loop
        for i in range(d-1, -1, -1):
            if slot_array[i] == 0:
                count += 1
                slot_array[i] = p
                break
    return count, sum(slot_array)
    



deadlines = [3, 1, 2, 2]
profits = [50, 10, 20, 30]
print(jobSequencing(profits, deadlines))

