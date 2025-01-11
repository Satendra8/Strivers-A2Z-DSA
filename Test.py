import heapq

def minimumEffortPath(heights):
    rows = len(heights)
    cols = len(heights[0])

    dist = [[float('inf')] * cols for _ in range(rows)]
    dist[0][0] = 0
    pqueue = [(0,0,0)]

    while pqueue:
        cost, i, j = pqueue.pop(0)

        #left
        if j-1 >= 0 and abs(heights[i][j] - heights[i][j-1]) < dist[i][j-1]:
            update_cost = max(cost, abs(heights[i][j] - heights[i][j-1]))
            if update_cost < dist[i][j-1]:
                dist[i][j-1] = update_cost
                pqueue.append((update_cost, i, j-1))

        #right
        if j+1 < cols and abs(heights[i][j] - heights[i][j+1]) < dist[i][j+1]:
            update_cost = max(cost, abs(heights[i][j] - heights[i][j+1]))
            if update_cost < dist[i][j+1]:
                dist[i][j+1] = update_cost
                pqueue.append((update_cost, i, j+1))

        #top
        if i-1 >= 0 and abs(heights[i][j] - heights[i-1][j]) < dist[i-1][j]:
            update_cost = max(cost, abs(heights[i][j] - heights[i-1][j]))
            if update_cost < dist[i-1][j]:
                dist[i-1][j] = update_cost
                pqueue.append((update_cost, i-1, j))

        #bottom
        if i+1 < rows and abs(heights[i][j] - heights[i+1][j]) < dist[i+1][j]:
            update_cost = max(cost, abs(heights[i][j] - heights[i+1][j]))
            if update_cost < dist[i+1][j]:
                dist[i+1][j] = update_cost
                pqueue.append((update_cost, i+1, j))

    return dist[rows-1][cols-1]


def minimumEffortPathOptimal(heights):
    """
    Dijkstra Algorithm
    1. take priority queue to store cost, i, j
    1. initialize a distance matrix with infinite
    2. initialize priority queue with 0,0 to 0
    3. move in all 4 directions
    4. if absolute difference is found less then already in dist then
    5. check if max(curr and absolute difference) still less then dist
    6. if less then update and push in pqueue
    Time Complexity: 4*M*N * log(M*N)
    Space Complexity: M*N
    """
    rows = len(heights)
    cols = len(heights[0])

    dist = [[float('inf')] * cols for _ in range(rows)]
    dist[0][0] = 0
    pqueue = []
    heapq.heappush(pqueue, (0,0,0))

    while pqueue:
        cost, i, j = heapq.heappop(pqueue)

        #left
        if j-1 >= 0 and abs(heights[i][j] - heights[i][j-1]) < dist[i][j-1]:
            update_cost = max(cost, abs(heights[i][j] - heights[i][j-1]))
            if update_cost < dist[i][j-1]:
                dist[i][j-1] = update_cost
                heapq.heappush(pqueue, (update_cost, i, j-1))

        #right
        if j+1 < cols and abs(heights[i][j] - heights[i][j+1]) < dist[i][j+1]:
            update_cost = max(cost, abs(heights[i][j] - heights[i][j+1]))
            if update_cost < dist[i][j+1]:
                dist[i][j+1] = update_cost
                heapq.heappush(pqueue, (update_cost, i, j+1))

        #top
        if i-1 >= 0 and abs(heights[i][j] - heights[i-1][j]) < dist[i-1][j]:
            update_cost = max(cost, abs(heights[i][j] - heights[i-1][j]))
            if update_cost < dist[i-1][j]:
                dist[i-1][j] = update_cost
                heapq.heappush(pqueue, (update_cost, i-1, j))

        #bottom
        if i+1 < rows and abs(heights[i][j] - heights[i+1][j]) < dist[i+1][j]:
            update_cost = max(cost, abs(heights[i][j] - heights[i+1][j]))
            if update_cost < dist[i+1][j]:
                dist[i+1][j] = update_cost
                heapq.heappush(pqueue, (update_cost, i+1, j))

    return dist[rows-1][cols-1]



heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
print(minimumEffortPathOptimal(heights))
