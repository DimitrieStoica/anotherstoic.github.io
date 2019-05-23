import heapq

array = [3, 2, 1, 5, 6, 4]
k = 2

#building heap runtime = O(n)

heap = []
for i in array:
    heapq.heappush(heap, i)
    if len(heap) > k:
        heapq.heappop(heap)

print(heap.pop(0))
