import heapq

def sumOfElements(arr, K1, K2):
    heap = []
    ans = 0

    for num in arr:
        heapq.heappush(heap, -num)
        if len(heap) > K2:
            heapq.heappop(heap)
    heapq.heappop(heap)
    while len(heap) > K1:
        ans += (-heapq.heappop(heap))
    return ans



arr = [10, 2, 50, 12, 48, 13]
K1 = 2
K2 = 6
print(sumOfElements(arr, K1, K2))