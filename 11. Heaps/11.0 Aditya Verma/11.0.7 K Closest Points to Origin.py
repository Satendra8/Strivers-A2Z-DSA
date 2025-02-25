"""
Q. Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

Example 1:

Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].
Example 2:

Input: points = [[3,3],[5,-1],[-2,4]], k = 2
Output: [[3,3],[-2,4]]
Explanation: The answer [[-2,4],[3,3]] would also be accepted.
"""
import heapq
def kClosest(points, k):
    """
    use MAX HEAP
    1. Euclidean distance = √(x1 - x2)2 + (y1 - y2)2)
    2. In our case second coordinate is origin (0,0)
    3. final formula  = √(x1)2 + (y1)2)
    4. If we don't do sqrt, then it will not affect ans, so remove this to reduce complexity
    Time Complexity: O(nlogk)
    Space Complexity: O(n)
    """
    heap = []

    for point in points:
        heapq.heappush(heap, (-(point[0]*point[0] + point[1]*point[1]), point))
        if len(heap) > k:
            heapq.heappop(heap)
    ans = []
    while heap:
        ans.append(heapq.heappop(heap)[1])
    return ans

points = [[3,3],[5,-1],[-2,4]]
k = 2
print(kClosest(points, k))