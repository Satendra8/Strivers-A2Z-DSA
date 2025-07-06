"""
Q. 621. Task Scheduler
Medium
Topics
premium lock icon
Companies
Hint
You are given an array of CPU tasks, each labeled with a letter from A to Z, and a number n. Each CPU interval can be idle or allow the completion of one task. Tasks can be completed in any order, but there's a constraint: there has to be a gap of at least n intervals between two tasks with the same label.

Return the minimum number of CPU intervals required to complete all tasks.

Example 1:

Input: tasks = ["A","A","A","B","B","B"], n = 2

Output: 8

Explanation: A possible sequence is: A -> B -> idle -> A -> B -> idle -> A -> B.

After completing task A, you must wait two intervals before doing A again. The same applies to task B. In the 3rd interval, neither A nor B can be done, so you idle. By the 4th interval, you can do A again as 2 intervals have passed.

Example 2:

Input: tasks = ["A","C","A","B","D","B"], n = 1

Output: 6

Explanation: A possible sequence is: A -> B -> C -> D -> A -> B.

With a cooling interval of 1, you can repeat a task after just one other task.

Example 3:

Input: tasks = ["A","A","A", "B","B","B"], n = 3

Output: 10

Explanation: A possible sequence is: A -> B -> idle -> idle -> A -> B -> idle -> idle -> A -> B.

There are only two types of tasks, A and B, which need to be separated by 3 intervals. This leads to idling twice between repetitions of these tasks.
"""
"""
Mark Revisit
"""
import heapq
import queue

def leastInterval(tasks, n):
    """
    1. Don't bother about tasks just consider frequency
    2. use a heap and a queue (similar like nodejs event loop, execution context and micro queue)
    3. store the frequency in heap
    4. pop from heap and store in queue with cooling down period (frequncy-1, time+n)
    5. if cooling down period overs, pop from queue and again put into heap
    6. keep doing this till both heap and queue becomes empty
    Time Complexity: O(n+k), k = inteval b/w 2 tasks
    Space Complexity: O(n)
    """
    d = {}
    for task in tasks:
        if task in d:
            d[task] += 1
        else:
            d[task] = 1
    max_heap = [-count for count in d.values()]
    heapq.heapify(max_heap)
    time = 0
    q = queue.deque()

    while q or max_heap:
        time += 1
        if max_heap:
            cnt = heapq.heappop(max_heap) + 1
            if cnt:
                q.append((cnt, time+n))

        if q and q[0][1] == time:
            heapq.heappush(max_heap, q.popleft()[0])
    return time


tasks = ["A","A","A", "B","B","B"]
n = 3
print(leastInterval(tasks, n))