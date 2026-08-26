class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = []
        for s in stones:
            heapq.heappush(maxHeap,-s)
        while len(maxHeap) > 1:
            y, x = heapq.heappop(maxHeap), heapq.heappop(maxHeap)
            print(y,x)
            if y < x:
                heapq.heappush(maxHeap,(y-x))
        return -maxHeap[0] if maxHeap else 0