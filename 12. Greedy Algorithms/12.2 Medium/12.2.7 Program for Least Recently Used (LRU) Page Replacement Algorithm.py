"""
Q. In operating systems that use paging for memory management, page replacement algorithm is needed to decide which page needs to be replaced when the new page comes in. Whenever a new page is referred and is not present in memory, the page fault occurs and Operating System replaces one of the existing pages with a newly needed page.

Given a sequence of pages in an array pages[] of length N and memory capacity C, find the number of page faults using Least Recently Used (LRU) Algorithm. 

Note:- Before solving this example revising the OS LRU cache mechanism is recommended.

Example 1:

Input: N = 9, C = 4
pages = {5, 0, 1, 3, 2, 4, 1, 0, 5}
Output: 8
Explaination: memory allocated with 4 pages 5, 0, 1, 
3: page fault = 4
page number 2 is required, replaces LRU 5: 
page fault = 4+1 = 5
page number 4 is required, replaces LRU 0: 
page fault = 5 + 1 = 6
page number 1 is required which is already present: 
page fault = 6 + 0 = 6
page number 0 is required which replaces LRU 3: 
page fault = 6 + 1 = 7
page number 5 is required which replaces LRU 2: 
page fault = 7 + 1  = 8.
"""

def LRU(N, C, pages):
    """
    Optimal Approach
    pages = [5, 0, 1, 3, 2, 4, 1, 0, 5]
    cache = [5, 0, 1, 3, 2, 4, 1, 0, 5]
            x  x  r  x  x
    fault = 8
    
    1. store used elements in cache
    2. if element is already present in cache, renew it by removing and again inserting
    Time Complexity: O(N)
    Space Complexity: O(1)
    """
    cache = []
    fault = 0
    for i in range(N):
        if pages[i] not in cache:
            fault += 1
            if len(cache) == C:
                cache.pop(0)
        else:
            cache.remove(pages[i])
        cache.append(pages[i])
    return fault

N = 9
C = 4
pages = [5, 0, 1, 3, 2, 4, 1, 0, 5]
print(LRU(N, C, pages))